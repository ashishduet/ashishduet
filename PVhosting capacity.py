
#
import pandapower as pp

def violations(net):
    pp.runpp(net)
    if net.res_line.loading_percent.max() > 50:
        return (True, "Line \n Overloading")
    elif net.res_trafo.loading_percent.max() > 50:
        return (True, "Transformer \n Overloading")
    elif net.res_bus.vm_pu.max() > 1.04:
        return (True, "Voltage \n Violation")
    else:
        return (False, None)

    from numpy.random import choice

    def chose_bus(net):
        return choice(net.load.bus.values)

    from numpy.random import normal

    def get_plant_size_mw():
        return normal(loc=0.5, scale=0.05)

    import pandapower.networks as nw
    def load_network():
        return nw.mv_oberrhein(scenario="generation")

    import pandas as pd

    iterations = 50
    results = pd.DataFrame(columns=["installed", "violation"])

    for i in range(iterations):
        net = load_network()
        installed_mw = 0
        while 1:
            violated, violation_type = violations(net)
            if violated:
                results.loc[i] = [installed_mw, violation_type]
                break
            else:
                plant_size = get_plant_size_mw()
                pp.create_sgen(net, chose_bus(net), p_mw=plant_size, q_mvar=0)
                installed_mw += plant_size

                import matplotlib.pyplot as plt
                plt.rc('xtick', labelsize=18)  # fontsize of the tick labels
                plt.rc('ytick', labelsize=18)  # fontsize of the tick labels
                plt.rc('legend', fontsize=18)  # fontsize of the tick labels
                plt.rc('axes', labelsize=20)  # fontsize of the tick labels
                plt.rcParams['font.size'] = 20


