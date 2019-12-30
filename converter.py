from  solve_captcha import solve

def main(args):
    ruta='/home/gnusyscamus/desarrollo/workana/imagenx.jpg'
    r=solve(ruta)
    print (r)
    #parse_captcha(ruta)
    #crack('imagenx')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
