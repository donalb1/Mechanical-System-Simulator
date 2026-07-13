import numpy as np
from scipy.integrate import solve_ivp

def run_simulation(mass, damping, stiffness, x0, v0, duration):
    def dynamics(t, y):
        x, v = y
        dxdt = v
        dvdt = -(damping/mass)*v - (stiffness/mass)*x
        return [dxdt, dvdt]

    t_span = (0, duration)
    y0 = [x0, v0]
    t_eval = np.linspace(0, duration, 500)
    sol = solve_ivp(dynamics, t_span, y0, t_eval=t_eval)

    return {
        "time": sol.t.tolist(),
        "displacement": sol.y[0].tolist(),
        "velocity": sol.y[1].tolist()
    }
