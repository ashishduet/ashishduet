
import pandapower as pp
net=pp.create_empty_network(name="Empty")
#create buses
b1=pp.create_bus(net,vn_kv=11.,name="Bus 1")
b2=pp.create_bus(net,vn_kv=.4,name="Bus 2")
b3=pp.create_bus(net,vn_kv=.4,name="Bus 3")

#External grid
pp.create_ext_grid(net,b1,vm_pu=1.02,name="External grid")

#create transformer
pp.create_transformer(net,b1,b2,"0.4 MVA 20/0.4 kV")

#create line
pp.create_line(net,b2,b3,std_type="NAYY 4x50 SE",length_km=0.15,name="Line")

#create load
pp.create_load(net,b3,p_mw=0.15,q_mvar=0.10)
pp.runpp(net)
print(net.res_bus)












