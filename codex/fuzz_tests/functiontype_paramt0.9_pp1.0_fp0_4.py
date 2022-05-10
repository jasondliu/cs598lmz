from types import FunctionType
list(FunctionType(input_rate,input_time).parameter_solver())

# Simulate the system with feedback control
time = linspace(0,1,1000)
signal = FunctionType(input_rate,input_time).signal()
system = FunctionType(input_rate,input_time).system()
output = system.T.sim(time,signal)
plot(time,output)
title("The output of the system with feedback control")
ylabel("y")
xlabel("time")
grid()
show()


# Simulate the system without feedback control
input = FunctionType(input_rate,input_time).signal()
plot(time,input)
title("The input of the system without feedback control")
ylabel("x")
xlabel("time")
grid()
show()

# Get the impulse of the plant
impulse = system[1].impulse()
plot(time,impulse)
title("The impulse of the plant")
ylabel("e")
xlabel("time")
grid()
show()

# Check the system with the final time and the amplitude

