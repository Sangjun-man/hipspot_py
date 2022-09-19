def rgbToGray(rgb):

    print(rgb)
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]

    Y = 0.2126*R + 0.7152*G + 0.0722*B

    return Y
