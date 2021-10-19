
#plotting a network
import pandapower.networks as nw
from pandapower.plotting import simple_plot, simple_plotly,pf_res_plotly
net=nw.mv_oberrhein()
simple_plot(net)

#plotting with matplotlib
import pandapower.plotting as plot
import pandapower.networks as nw

# load example net (IEEE 9 buses)
net = nw.mv_oberrhein()
# simple plot of net with existing geocoordinates or generated artificial geocoordinates
plot.simple_plot(net, show_plot=True)

