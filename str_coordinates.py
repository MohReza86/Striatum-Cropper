

######### Functions below return the coordinates of the "rostral" division of striatum  #########

def int_pts_inj_rost(width, height):
    # rostral striatum (injected hemisphere) coordinates --> left hemisphere (mouse POV)
    int_pts_inj_rost = [[int(width*0.658), int(height*0.362)], [int(width*0.681), int(height*0.358)], 
    [int(width*0.701), int(height*0.36)],[int(width*0.751), int(height*0.395)],[int(width*0.777), int(height*0.444)], 
    [int(width*0.777), int(height*0.52)],[int(width*0.773), int(height*0.631)], [int(width*0.762), int(height*0.676)], 
    [int(width*0.748), int(height*0.702)],[int(width*0.717), int(height*0.66)], [int(width*0.673), int(height*0.61)],
    [int(width*0.634), int(height*0.58)], [int(width*0.598), int(height*0.56)], [int(width*0.600), int(height*0.44)],
    [int(width*0.628), int(height*0.401)]]

    return int_pts_inj_rost

def int_pts_non_inj_rost(width, height):
# rostral striatum (non_injected hemisphere) coordinates --> right hemisphere (mouse POV)
    int_pts_non_inj_rost = [[int(width*0.399), int(height*0.448)], [int(width*0.331), int(height*0.368)],
    [int(width*0.27), int(height*0.417)],[int(width*0.231), int(height*0.475)], 
    [int(width*0.231), int(height*0.59)], [int(width*0.253), int(height*0.707)], 
    [int(width*0.32), int(height*0.617)], [int(width*0.399), int(height*0.563)]]

    return int_pts_non_inj_rost

def int_pts_cc_rost(width, height):
# corpus collasum coordinates --> right hemisphere (mouse POV)
    rost_pts_cc = [[int(width*0.331), int(height*0.368)],[int(width*0.27), int(height*0.417)],[int(width*0.231), int(height*0.475)], 
    [int(width*0.227), int(height*0.376)],[int(width*0.321), int(height*0.29)]]

    return rost_pts_cc


####### Functions below return the coordinates of the "caudal" division of striatum  #########

def caudal_pts_inj(width, height):
    # caudal striatum (injected hemisphere) coordinates --> left hemisphere (mouse POV)
    caudal_pts_inj = [[int(width*0.63), int(height*0.24)], [int(width*0.72), int(height*0.28)], [int(width*0.8), int(height*0.35)],
    [int(width*0.85), int(height*0.45)], [int(width*0.88), int(height*0.572)], [int(width*0.855), int(height*0.683)],
    [int(width*0.812), int(height*0.756)], [int(width*0.775), int(height*0.756)], [int(width*0.75), int(height*0.733)],
    [int(width*0.78), int(height*0.653)], [int(width*0.77), int(height*0.552)], [int(width*0.74), int(height*0.505)],
    [int(width*0.735), int(height*0.484)], [int(width*0.69), int(height*0.424)], [int(width*0.658), int(height*0.344)],
    [int(width*0.677), int(height*0.362)]]

    return caudal_pts_inj

def caudal_pts_non_inj(width, height):
# caudal striatum (non_injected hemisphere) coordinates --> right hemisphere (mouse POV)
    caudal_pts_non_inj = [[int(width*0.302), int(height*0.276)], [int(width*0.166), int(height*0.394)],
    [int(width*0.113), int(height*0.583)], [int(width*0.16), int(height*0.756)], [int(width*0.238), int(height*0.706)],
    [int(width*0.201), int(height*0.577)], [int(width*0.262), int(height*0.434)],
    [int(width*0.33), int(height*0.427)]]

    return caudal_pts_non_inj

def caudal_pts_cc(width, height):
# corpus collasum coordinates --> right hemisphere (mouse POV)
    caudal_pts_cc = [[int(width*0.302), int(height*0.276)], [int(width*0.166), int(height*0.394)], 
    [int(width*0.175), int(height*0.361)], [int(width*0.304), int(height*0.243)]]

    return caudal_pts_cc



#### coordinates of the divisions within the rostrial striatum 


r_m = [[0, int(height*0.058)], [int(width*0.391), int(height*0.364)], [0, int(height*0.728)]]
r_imd = [[0,0], [0, int(height*0.058)], [int(width*0.391), int(height*0.364)],[int(width*0.573), int(height*0.397)], [width, int(height*0.192)], [width, 0]]
r_l_ls = [[width, int(height*0.192)], [int(width*0.573), int(height*0.397)], [int(width*0.58), int(height*0.525)], [width, int(height*0.74)]]
r_l_vm = [[0, int(height*0.87)],[int(width*0.58), int(height*0.525)],[width, int(height*0.74)], [width, height], [int(width*0.833), height]]
r_imv = [[0, int(height*0.87)], [int(width*0.58), int(height*0.525)], [int(width*0.573), int(height*0.397)], [int(width*0.391), int(height*0.364)], [0, int(height*0.728)]]


#### coordinates of the divisions within the caudal striatum 

c_d_dm = [[0, int(height*0.459)], [0,0], [int(width*0.251), 0], [int(width*0.325), int(height*0.322)]]
c_d_dl = [[int(width*0.251), 0], [int(width*0.325), int(height*0.322)], [int(width*0.435), int(height*0.333)], [width, int(height*0.064)]]
c_i_d = [[width, int(height*0.064)], [int(width*0.435), int(height*0.333)], [int(width*0.534), int(height*0.496)], [int(width*0.632), int(height*0.481)], [width, int(height*0.302)]]
c_i_vl = [[width, int(height*0.302)], [int(width*0.632), int(height*0.481)], [int(width*0.829), int(height*0.631)], [width, int(height*0.63)]]
c_v = [[width, height], [width, int(height*0.63)], [int(width*0.829), int(height*0.631)], [0, int(height*0.863)],[0, height]]
c_i_vm = [[0, int(height*0.863)], [int(width*0.829), int(height*0.631)], [int(width*0.632), int(height*0.481)], 
[int(width*0.534), int(height*0.496)], [0, int(height*0.97)]]
c_d_vm = [[0, int(height*0.97)], [int(width*0.534), int(height*0.496)], [int(width*0.435), int(height*0.333)], 
[int(width*0.325), int(height*0.322)], [0, int(height*0.459)]]