gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_frame.f_lasti
try:
    gi.gi_frame.f_lasti
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_frame.f_locals
try:
    gi.gi_frame.f_locals
except AttributeError:
    pass
else:
    print('AttributeError expected')
gi_gi_code_gi_frame_gi_frame_f_lasti_gi_frame_f_locals_a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_aa_ab
