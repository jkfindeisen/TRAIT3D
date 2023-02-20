"""
Loads and processes 3D data instead 2D data
"""

import pathlib

import pandas as pd

from trait2d.analysis import Track

if __name__ == '__main__':
    file = pathlib.Path(__file__).parent / 'example_data_3d.csv'
    df = pd.read_csv(file)
    ids = df['id'].unique()
    tracks = []
    for id in ids:
        tracks.append(Track.from_dataframe(df, 'x (m)', 'y (m)', 'z (m)', 't (s)', 'id', 'metres', 'seconds', id))
    for track in tracks:
        n = len(track.get_x())
        print('length {}'.format(n))
        track.adc_analysis(fraction_fit_points=0.99)
        track.msd_analysis(fraction_fit_points=0.99)
        track.get_msd_analysis_results()
        track.get_msd()
        track.plot_msd()
        results = track.get_adc_analysis_results()['best_model']
        print(results)
        track.plot_trajectory()
        track.plot_adc_analysis_results()
        track.plot_msd_analysis_results()
        pass

