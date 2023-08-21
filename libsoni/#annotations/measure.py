import pandas as pd
import numpy as np
from libsoni.util.utils import click, load_sample, add_to_sonification
import os


def sonify_measure_annotation(path_to_csv: str,
                              sonification_method: str = 'click',
                              pitch: int = 69,
                              sample: str = '',
                              amplitude: float = 1.0,
                              duration: float = 0.2,
                              fs: int = 44100) -> np.ndarray:
    """
    This function sonifies the entries of a measure annotation in .csv format.

    Parameters
    ----------
    path_to_csv : str
        path to annotation file
    sonification_method : str, default: 'click'
        sonification method, either 'click' or 'sample'
    pitch : int, default: 69
        pitch for click signal
    sample : str, default: ''
        path to the desired sample
    amplitude : float, default: 1.0
        amplitude for click signal
    duration : float, default: 0.2
        duration (in seconds) for click signal
    fs : int, default: 44100
        Sampling rate (in samples per second)

    Returns
    ----------
    y: array-like
        Sonified measure annotation
    """

    # read annotation file
    measure_annotation_df = pd.read_csv(os.path.join(path_to_csv), delimiter=';')

    # create empty array according to the time bounds given by the annotation file
    y = np.zeros(np.ceil((max(measure_annotation_df.start.unique() + duration) * fs)).astype(int))

    if sonification_method == 'click':

        # create click-signal for measure events
        measure_signal = click(pitch=pitch, amplitude=amplitude, duration=duration, fs=fs)

    elif sonification_method == 'sample':

        # load sample
        measure_signal, _ = load_sample(sample, fs)

    # iterate measure events of the annotation file and insert corresponding click signals at the corresponding temporal positions
    for i, r in measure_annotation_df.iterrows():
        start, _ = r
        # add measure_signal to sonification
        y = add_to_sonification(sonification=y, sonification_for_event=measure_signal, start=start, fs=fs)

    return y