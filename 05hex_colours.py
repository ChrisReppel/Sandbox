"""
Chris Reppel
Prac 5
"""

COLOUR_CODES = {"AliceBlue": "#F0F8FF", "Aqua": "#00FFFF",
                "chartreuse1": "#7FFF00", "CornflowerBlue": "#6495ED",
                "cyan1": "#00FFFF", "DarkOrchid": "#9932CC",
                "DarkSeaGreen1": "#C1FFC1", "DarkTurquoise": "#00CED1",
                "DarkViolet": "#9400D3", "DeepPink1": "#FF1493",
                "DeepSkyBlue2": "#00B2EE", "DodgerBlue1": "#1E90FF", "firebrick1": "#FF3030",
                "gold1": "#FFD700", "LawnGreen": "#7CFC00"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")