def calculate_target_error(frame_width, frame_height, x_min, y_min, x_max, y_max):
    frame_center_x = frame_width / 2
    frame_center_y = frame_height / 2

    target_center_x = (x_min + x_max) / 2
    target_center_y = (y_min + y_max) / 2

    x_error = target_center_x - frame_center_x
    y_error = target_center_y - frame_center_y

    return x_error, y_error

x_error, y_error = calculate_target_error(
    frame_width=640,
    frame_height=480,
    x_min=120,
    y_min=80,
    x_max=200,
    y_max=160,
)

print(f"x_error: {x_error}")
print(f"y_error: {y_error}")