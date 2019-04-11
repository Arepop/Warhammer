new_spells = list()

with open("spells.txt", 'r') as spells:
    lines = spells.readlines()
    for line in lines:
        line = line.replace("o ___ ___ ", "").replace(
            " N_ ", ";N;").replace(" Y_ ", ";Y;").replace(" Sp_. ", ";Sp_.;")
        line = line.replace(" C_o_ ", ";Co;").replace(" T_r_ ", ";Tr;").replace(
            " _U_n ", ";Un;").replace(" E_v_ ", ";Ev;").replace(
            " E_n_ ", ";En;").replace(" I_l_ ", ";Il;").replace(
            " _N_e ", ";Ne;").replace(" _A_b ", ";Ab;").replace(
            " D_i_ ", ";Di;").replace(" C_o_/Ev ", ";Co/Ev;").replace(" C_o_/Ne ", ";Co/Ne;")
        line = line.replace(" 1 _a_ct ", ";1 act;").replace(
            " 10__ m__in_ ", ";10 min;").replace(
            " Sw__if_t__ ", ";Swift;").replace(
            " 1 _rou_n_d ", ";1 round;"). replace(
            " Im__m_ed. ", ";Immed.;").replace(
            " 1 _m_in__ ", ";1 min;").replace(
            " 1 _h_o_u_r_ ", ";1 hour;")
        line = line.replace("To_u_c_h__ ", ";Touch;").replace(
            "C_lo_se___ ", ";Close;").replace(
            "Pers_o_n_a_l ", ";Personal;").replace(
            "M_e_d_i_u_m_ ", ";Medium;").replace(
            "Lo_n_g___ ", ";Long;").replace(
            " Personal;", ";Personal;")
        line = line.replace(" -_______", ";-;").replace(
            " W_ill n_. ", ";Will n.;").replace(
            " W_ill dis_.", ";Will dis.;").replace(
            " Fo_r n_.", ";For n.;").replace(
            " W_ill part_.", ";Will part.;").replace(
            "Sp_e_c_ial", ";Special;").replace(
            "R_e_f _n_.", ";Ref n.;").replace(
            "R_e_f _Â˝", ";Ref half.;").replace(
            "R_e_f _p_a_rt_.", ";Ref part.;").replace(
            " Fo_r p_a_rt.", ";Fort part.;").replace(
            "Fo_r Â˝", ";For half.;")
        line = line.replace("_", "").replace("\n", "")
        line = line.replace("BVD", ";BVD").replace(
            "PHB", ";PHB").replace("SpC", ";SpC").replace(
            "SaSt", ';SaSt').replace("CM.", ";CM.").replace(
            "DM.", ';DM.').replace("FoE.", ";FoE.").replace(
            "DrU.", ";DrU.").replace("CS.", ";CS.").replace(
            "EE.", ";EE.").replace("MoE.", ";MoE.").replace(
            "ShS.", ";ShS.").replace("ToM.", ";ToM.").replace(
            "HoH.", ";HoH.").replace("PH2.", ";PH2.").replace(
            "RoDr.", ";RoDr.").replace("Cts.", ";Cts.").replace(
            "RoD.", ";Rod.").replace("DrM.", ";DrM.").replace(
            "RoE.", ";RoE.").replace("FB.", ";FB.").replace(
            "BED.", ";BED.").replace("LM.", ";LM.").replace(
            "UE.", ";UE.").replace("FoW.", ";FoW.").replace(
            "SW.", ";SW.").replace("MoF.", ";MoF.").replace(
            "EoF.", ";EoF.").replace("LoM.", ";LoM.").replace(
            "Und.", ";Und.").replace("LEoF.", ";LEoF.").replace(
            "HoB.", ";HoB.").replace("FC1.", ";FC1.").replace(
            "FC2.", ";FC2.").replace("CoV.", ";CoV.").replace(
            "PiGntE.", ";PiGntE.").replace("SK.", ";SK.").replace(
            "RoW.", ";RoW.").replace("CoR.", ";CoR.").replace(
            "SoS.", ";SoS.").replace("MM5.", ";MM5.").replace(
            "PoF.", ";PoF.").replace("SCoT.", ";SCoT.").replace(
            "DoF.", ";DoF.").replace("PGtE.", ";PGtE.").replace(
            "EUM.", ";EUM.").replace("WoL.", ";WoL.").replace(
            "RoF.", ";RoF.").replace("LoD.", ";LoD.").replace(
            "RoS.", ";Ros.")
        line = line.replace(
            "; ", ";").replace("; ;", ";").replace(";;", ";").replace(
            " ft", " ft;", 1).replace("Will Â˝.", ";Will half.").replace(
            " -/", " ;")
        new_spells.append(line)

with open("spells_new.txt", "w") as spells:
    spells.writelines(f'{l}\n' for l in new_spells)
