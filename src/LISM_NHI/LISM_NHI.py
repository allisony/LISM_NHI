import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np
from . import PACKAGEDIR
from LISM_NHI import config_parser



class LISM_NHI_map:

    def __init__(self, config_filename=f"{PACKAGEDIR}/data/configuration_file.txt"):
        
        self.config_filename = config_filename
        self.config = self.__read_config(config_filename)

    def __read_config(self, config_filename):
        return config_parser.Config(config_filename)

    def generate_coordinate_grids(self):

        phi = np.linspace(0, 2.*np.pi, self.config.phi_len)
        theta = np.linspace(-0.5 * np.pi, 0.5 * np.pi, self.config.theta_len)
        phi_grid, theta_grid = np.meshgrid(phi, theta, indexing="ij")
        phi_grid = phi_grid.flatten()
        theta_grid = theta_grid.flatten()
        X_grid = np.vstack((phi_grid,theta_grid))

        grid_skycoord_catalog = SkyCoord(X_grid[0,:]*u.radian,X_grid[1,:]*u.radian,frame='icrs')

        return grid_skycoord_catalog

#    def create_skycoord_object_for_star(self, RA, Dec, frame='icrs', units=u.deg):

#        assert (RA is float) and (Dec is float), "string inputs for RA/Dec not enabled. Must input degrees as float"

#        coord = SkyCoord(RA * units, Dec * units, frame=frame)

#        return coord

    def input_star_info(self, skycoord_obj, distance):

        assert (distance <= 100.), "maps are valid only for stellar distances <= 100 pc"

        if distance <= 10:

            which_map = "all_inside_10pc"

        elif (distance > 10) & (distance <= 20):

            which_map = "10_20 pc"

        elif (distance > 20) & (distance <= 30):

            which_map = "20_30 pc"

        elif (distance > 30) & (distance <= 50):

            which_map = "30_50 pc"

        elif (distance > 50) & (distance <= 70):

            which_map = "50_70 pc"

        elif (distance > 70) & (distance <= 100):

            which_map = "70_100 pc"

        return skycoord_obj, which_map

    def find_nearest_grid_element(self, grid_skycoord_catalog, skycoord_obj):

        nearest_grid_index, sep2d, dist3d = skycoord_obj.match_to_catalog_3d(grid_skycoord_catalog, 1)

        return nearest_grid_index


    def read_in_NHI_map(self, which_map):

        #df = pd.read_csv(file_path+'Bestfit_hyperparameters_' + which_map + '_upperlowerlimits.csv')

        #stars = np.loadtxt(file_path+'NHI_column_fitted_stars_' + which_map + '_upperlowerlimits.txt')

        NHI_map = np.loadtxt(file_path+'NHI_column_map_' + which_map + '_upperlowerlimits.txt')

        return NHI_map[:,1] # return median values


    def get_nearest_NHI_map_value(self, NHI_map, nearest_grid_index):

        return NHI_map[nearest_grid_index]



        


