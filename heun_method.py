import math
def f(expression, x, y):

    allowed_names = {

        "x": x,
        "y": y,

        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,

        "sqrt": math.sqrt,
        "log": math.log,
        "exp": math.exp,

        "pi": math.pi,
        "e": math.e
    }

    expression = expression.replace("^", "**")
    expression = expression.replace("x2", "x**2")
    expression = expression.replace("y2", "y**2")

    try:
        return eval(
            expression,
            {"__builtins__": {}},
            allowed_names
        )

    except Exception:
        return 0


def heun_method(expression, x0, y0, h, target):

    steps = []

    x = x0
    y = y0

    n_steps = int((target - x0) / h)

    for n in range(n_steps):

        # STEP 1
        slope_start = f(expression, x, y)

        # STEP 2
        predictor = y + h * slope_start

        # STEP 3
        x_next = x + h

        # STEP 4
        slope_end = f(expression, x_next, predictor)

        # STEP 5
        y_next = y + (h / 2) * (slope_start + slope_end)

        # SAVE COMPLETE DATA
        steps.append({

            "n": n,

            "x": round(x, 6),

            "y": round(y, 6),

            "h": round(h, 6),

            "x_next": round(x_next, 6),

            "slope_start": round(slope_start, 6),

            "predictor": round(predictor, 6),

            "slope_end": round(slope_end, 6),

            "y_next": round(y_next, 6)

        })

        # UPDATE VALUES
        x = x_next
        y = y_next

    return round(y, 6), steps