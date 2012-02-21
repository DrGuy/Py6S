from Py6S import *

s = SixS()
s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
s.solar_z = 30
s.solar_a = 0

res = IOHelpers.all_angles(s)
o = IOHelpers.extract_output(res, 'pixel_reflectance')
IOHelpers.plot_all_angles(o)