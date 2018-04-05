
#subimage_size =  740     # size of subimages
#subimage_border = 10     # border around subimage to avoid edge effects
subimage_size = 2960     # size of subimages
subimage_border =  0     # border around subimage to avoid edge effects

# background estimation: these are the optional methods to estimate the
# backbround and its standard deviation (STD):
# (1) background and STD/RMS map determined by SExtractor (fastest)
# (2) improved background and STD map using masking of all sources (recommended)
# (3) similar to 2 but using photutils' Background2D (very very slow!)
bkg_method = 2           # background method to use
bkg_nsigma = 3           # data outside mean +- nsigma * stddev are
                         # clipped; used in methods 1, 3 and 4
bkg_boxsize = 592        # size of region used to determine
                         # background in methods 2, 3 and 4
bkg_filtersize = 3       # size of filter used for smoothing the above
                         # regions for method 2, 3 and 4

# ZOGY parameters
fratio_local = True      # determine fratio (Fn/Fr) from subimage (T) or full frame (F)
dxdy_local = False       # determine dx and dy from subimage (T) or full frame (F)
transient_nsigma = 6     # required significance in Scorr for transient detection

# optional fake stars
nfakestars = 0           # number of fake stars to be added to each subimage
                         # if 1: star will be at the center, if > 1: randomly distributed
fakestar_s2n = 10        # required signal-to-noise ratio of the fake stars    

# switch on/off different functions
dosex = False            # do extra SExtractor run (already done inside Astrometry.net)
dosex_psffit = False     # do extra SExtractor run with PSF fitting

# header keywords from which certain values are taken; these should be
# present in the header, but the names can be changed here
key_gain = 'GAIN'
key_ron = 'RDNOISE'
key_satlevel = 'SATURATE'
key_ra = 'SW_RA'
key_dec = 'SW_DEC'
key_pixscale = 'PIXSCALE'
key_exptime = 'EXPTIME'


# for seeing estimate
fwhm_imafrac = 0.25      # fraction of image area that will be used
                         # for initial seeing estimate
fwhm_detect_thresh = 10. # detection threshold for fwhm SExtractor run
fwhm_class_sort = False  # sort objects according to CLASS_STAR (T)
                         # or by FLUX_AUTO (F)
fwhm_frac = 0.25         # fraction of objects, sorted in brightness
                         # or class_star, used for fwhm estimate

# WCS
skip_wcs = True          # skip Astrometry.net step if image already
                         # contains a reliable WCS solution
                         
# PSF parameters
use_single_psf = False   # use the same central PSF for all subimages
psf_clean_factor = 0     # pixels with values below (PSF peak * this
                         # factor) are set to zero; if this parameter
                         # is zero, no cleaning is done
psf_radius = 5           # PSF radius in units of FWHM used to build the PSF
                         # this determines the PSF_SIZE in psfex.config
                         # and size of the VIGNET in sex.params

psf_sampling = 0.0       # PSF sampling step in image pixels used in PSFex
                         # If zero, it is automatically determined for the
                         # new and ref image as:
                         #    psf_sampling = FWHM * [psf_samp_fwhmfrac]
                         # If non-zero, its value is using for the sampling
                         # step in both images.
psf_samp_fwhmfrac = 1/4.5 # PSF sampling step in units of FWHM
                         # this is only used if [psf_sampling]=0.
                         
# Astrometry.net's tweak order
astronet_tweak_order = 3

# Photometric calibration
obs_lat = -32.38722      # degrees (North)
obs_long = 20.81667      # degrees (East)
obs_height = 1798.       # meters above sealevel
# these [ext_coeff] are very rough extinction estimates for SAAO; update!
ext_coeff = {'u':0.4, 'g':0.2, 'q':0.15, 'r':0.1, 'i':0.1, 'z':0.1}
cal_cat = ''

# path and names of configuration files
cfg_dir = './Config/'
sex_cfg = cfg_dir+'sex.config'               # SExtractor configuration file
sex_cfg_psffit = cfg_dir+'sex_psffit.config' # same for PSF-fitting version
sex_cfg_trans = cfg_dir+'sex_trans.config'   # same for transient detection version
sex_par = cfg_dir+'sex.params'               # SExtractor output parameters definition file
sex_par_psffit = cfg_dir+'sex_psffit.params' # same for PSF-fitting version
sex_par_ref = cfg_dir+'sex_ref.params'       # same for reference image output version
sex_par_trans = cfg_dir+'sex_trans.params'   # same for transient output version
psfex_cfg = cfg_dir+'psfex.config'           # PSFex configuration file
swarp_cfg = cfg_dir+'swarp.config'           # SWarp configuration file

apphot_radii = [0.66, 1.5, 5] # list of radii in units of FWHM
                              # used for aperture photometry
                              # in SExtractor general

redo = True              # execute functions even if output file exist
verbose = True           # print out extra info
timing = True            # (wall-)time the different functions
display = False          # show intermediate fits images (centre and 4 corners)
make_plots = True        # make diagnostic plots and save them as pdf
show_plots = False       # show diagnostic plots