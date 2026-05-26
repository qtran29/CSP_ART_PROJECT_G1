import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("#F1CC84")
    
    # Halfcourt line
    sg.set_outline_color("white")
    sg.draw_line(300,0,300,400, 2)

    # draw circle for logo
    sg.set_line_thickness(10)
    sg.set_fill_color("#DC8535")
    sg.set_outline_color("#34569B")
    sg.fill_circle(300, 200, 60)

    # Draw Y
    sg.set_outline_color("black")
    sg.draw_line(300,250,300,195, 8)
    sg.draw_line(270,160,300,200, 8)
    sg.draw_line(330,160,300,200, 8)

    # Draw N
    sg.draw_line(260,175,260,225, 8)
    sg.draw_line(260,180,280,220, 8)
    sg.draw_line(280,175,280,225, 8)

    # Draw K
    sg.draw_line(320,175,320,225, 8)
    sg.draw_line(320,200,340,225, 8)
    sg.draw_line(320,200,340,175, 8)
    
    
    
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
