import configparser
import numpy as np
import os
from . import PACKAGEDIR

class Config:

    def __init__(self, filename):

        config = configparser.ConfigParser()
        print('Reading configuration file: {}'.format(filename))
        if os.path.isfile(filename): 
            config.read(filename)
        else: 
            raise Exception('Config file does not exist or path is incorrect.')


        # grid parameters
        self.phi_len = config['Grid information'].getint('phi length')
        self.theta_len = config['Grid information'].getint('theta length')




        self.encircled_energy_fraction = config['Instrument parameters'].getfloat('encircled energy fraction')
        self.spot_area = config['Instrument parameters'].get('spot area').split('*')
        self.spot_area = np.array([float(value) for value in self.spot_area]).prod() * self.dlam
        self.anticoincidence_factor = config['Instrument parameters'].getfloat('anti-coincidence factor')
        self.background_counts_per_area = config['Instrument parameters'].getfloat('background counts per area')
        self.background_margin_factor = config['Instrument parameters'].getfloat('background margin factor')
        self.scattered_light_counts_per_area = config['Instrument parameters'].getfloat('scattered light counts per area')
        self.airglow_counts_per_area = config['Instrument parameters'].getfloat('airglow counts per area')
        self.Aeff_margin_factor = config['Instrument parameters'].getfloat('Aeff margin factor')
        self.Aeff_filename = config['Instrument parameters'].get('Aeff filename')
        self.Aeff_threshold = config['Instrument parameters'].getfloat('Aeff threshold')

        # observation parameters
        self.SEEN_exptime = config['Observation parameters'].getfloat('SEEN exposure time')
        self.DEEP_exptime = config['Observation parameters'].getfloat('DEEP exposure time')
        self.convolve = config['Observation parameters'].getboolean('convolve?')

        # Lines for SNR calculations
        self.line_list = config['Lines for SNR calculations']


        # ISM parameters
        self.rel_he1 = config['ISM parameters'].getfloat('He I relative to H I')
        self.frac_he2 = config['ISM parameters'].getfloat('fraction of He in He II')

    if __name__ == "__main__":
        filename = f"{PACKAGEDIR}/data/configuration_file.txt"
        config = Config(filename)





