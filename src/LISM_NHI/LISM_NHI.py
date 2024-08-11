import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np
from . import PACKAGEDIR

def main(skycoord_obj, distance):

    skycoord_obj, which_map = input_star_info(skycoord_obj, distance)

    grid_skycoord_catalog, NHI_map = read_in_NHI_map(which_map)

    nearest_grid_index = find_nearest_grid_element(grid_skycoord_catalog, skycoord_obj)

    NHI = get_nearest_NHI_map_value(NHI_map, nearest_grid_index)

    return NHI




def generate_coordinate_grids(phi_len=200, theta_len=200):

    phi = np.linspace(0, 2.*np.pi, phi_len)
    theta = np.linspace(-0.5 * np.pi, 0.5 * np.pi, theta_len)
    phi_grid, theta_grid = np.meshgrid(phi, theta, indexing="ij")
    phi_grid = phi_grid.flatten()
    theta_grid = theta_grid.flatten()
    X_grid = np.vstack((phi_grid,theta_grid))

    grid_skycoord_catalog = SkyCoord(X_grid[0,:]*u.radian,X_grid[1,:]*u.radian,frame='icrs')

    return grid_skycoord_catalog


def input_star_info(skycoord_obj, distance):

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

def find_nearest_grid_element(grid_skycoord_catalog, skycoord_obj):

    nearest_grid_index, sep2d, dist3d = skycoord_obj.match_to_catalog_3d(grid_skycoord_catalog, 1)

    return nearest_grid_index


def read_in_NHI_map(which_map):

    #df = pd.read_csv(file_path+'Bestfit_hyperparameters_' + which_map + '_upperlowerlimits.csv')

    #stars = np.loadtxt(file_path+'NHI_column_fitted_stars_' + which_map + '_upperlowerlimits.txt')

    NHI_map = np.loadtxt(file_path+'NHI_column_map_' + which_map + '_upperlowerlimits.txt')

    grid_skycoord_catalog = generate_coordinate_grids()

    return grid_skycoord_catalog, NHI_map[:,1] # return median values


def get_nearest_NHI_map_value(NHI_map, nearest_grid_index):

    return NHI_map[nearest_grid_index]



        


