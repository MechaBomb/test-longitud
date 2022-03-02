from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/metro/<string:dato1>")
def get_datosM(dato1):
    dato = float(dato1)
    return jsonify({ "metro" : dato})

@app.route("/metrokilo/<string:dato1>")
def get_datosMK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.001
    return jsonify({ "kilometro" : dato2})

@app.route("/metrocenti/<string:dato1>")
def get_datosMC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*100
    return jsonify({ "centimetro" : dato2})

@app.route("/metromilla/<string:dato1>")
def get_datosMMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.0006213
    return jsonify({ "milla" : dato2})

@app.route("/metroyarda/<string:dato1>")
def get_datosMY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1.0936132
    return jsonify({ "yarda" : dato2})

@app.route("/metropie/<string:dato1>")
def get_datosMP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*3.2808398
    return jsonify({ "pie" : dato2})

@app.route("/metropulgada/<string:dato1>")
def get_datosMPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*39.3700787
    return jsonify({ "pulgada" : dato2})

@app.route("/kilo/<string:dato1>")
def get_datosK(dato1):
    dato = float(dato1)
    return jsonify({ "kilometro" : dato})

@app.route("/kilometro/<string:dato1>")
def get_datosKM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1000
    return jsonify({ "metro" : dato2})

@app.route("/kilocenti/<string:dato1>")
def get_datosKC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*100000
    return jsonify({ "centimetro" : dato2})

@app.route("/kilomilla/<string:dato1>")
def get_datosKMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.6213711
    return jsonify({ "milla" : dato2})

@app.route("/kiloyarda/<string:dato1>")
def get_datosKY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1093.6132983
    return jsonify({ "yarda" : dato2})

@app.route("/kilopie/<string:dato1>")
def get_datosKP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*3280.839895
    return jsonify({ "pie" : dato2})

@app.route("/kilopulgada/<string:dato1>")
def get_datosKPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*39370.07874
    return jsonify({ "pulgada" : dato2})

@app.route("/centi/<string:dato1>")
def get_datosC(dato1):
    dato = float(dato1)
    return jsonify({ "centimetro" : dato})

@app.route("/centikilo/<string:dato1>")
def get_datosCK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.00001
    return jsonify({ "kilometro" : dato2})

@app.route("/centimetro/<string:dato1>")
def get_datosCM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.01
    return jsonify({ "metro" : dato2})

@app.route("/centimilla/<string:dato1>")
def get_datosCMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.000006213
    return jsonify({ "milla" : dato2})

@app.route("/centiyarda/<string:dato1>")
def get_datosCY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.010936132
    return jsonify({ "yarda" : dato2})

@app.route("/centipie/<string:dato1>")
def get_datosCP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.032808398
    return jsonify({ "pie" : dato2})

@app.route("/centipulgada/<string:dato1>")
def get_datosCPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.393700787
    return jsonify({ "pulgada" : dato2})

@app.route("/milla/<string:dato1>")
def get_datosMi(dato1):
    dato = float(dato1)
    return jsonify({ "milla" : dato})

@app.route("/millakilo/<string:dato1>")
def get_datosMiK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1.609344
    return jsonify({ "kilometro" : dato2})

@app.route("/millacenti/<string:dato1>")
def get_datosMiC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*160934.4
    return jsonify({ "centimetro" : dato2})

@app.route("/millametro/<string:dato1>")
def get_datosMiM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1609.344
    return jsonify({ "metro" : dato2})

@app.route("/millayarda/<string:dato1>")
def get_datosMiY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*1760
    return jsonify({ "yarda" : dato2})

@app.route("/millapie/<string:dato1>")
def get_datosMiP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*5280
    return jsonify({ "pie" : dato2})

@app.route("/millapulgada/<string:dato1>")
def get_datosMiPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*63360
    return jsonify({ "pulgada" : dato2})

@app.route("/yarda/<string:dato1>")
def get_datosY(dato1):
    dato = float(dato1)
    return jsonify({ "yarda" : dato})

@app.route("/yardakilo/<string:dato1>")
def get_datosYK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.0009144
    return jsonify({ "kilometro" : dato2})

@app.route("/yardacenti/<string:dato1>")
def get_datosYC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*91.44
    return jsonify({ "centimetro" : dato2})

@app.route("/yardamilla/<string:dato1>")
def get_datosYMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.000568182
    return jsonify({ "milla" : dato2})

@app.route("/yardametro/<string:dato1>")
def get_datosYM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.9144
    return jsonify({ "metro" : dato2})

@app.route("/yardapie/<string:dato1>")
def get_datosYP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*3
    return jsonify({ "pie" : dato2})

@app.route("/yardapulgada/<string:dato1>")
def get_datosYPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*36
    return jsonify({ "pulgada" : dato2})

@app.route("/pie/<string:dato1>")
def get_datosP(dato1):
    dato = float(dato1)
    return jsonify({ "pie" : dato})

@app.route("/piekilo/<string:dato1>")
def get_datosPK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.0003048
    return jsonify({ "kilometro" : dato2})

@app.route("/piecenti/<string:dato1>")
def get_datosPC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*30.48
    return jsonify({ "centimetro" : dato2})

@app.route("/piemilla/<string:dato1>")
def get_datosPMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.000189394
    return jsonify({ "milla" : dato2})

@app.route("/pieyarda/<string:dato1>")
def get_datosPY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.33333333
    return jsonify({ "yarda" : dato2})

@app.route("/piemetro/<string:dato1>")
def get_datosPM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.3048
    return jsonify({ "metro" : dato2})

@app.route("/piepulgada/<string:dato1>")
def get_datosPPu(dato1):
    dato1 = float(dato1)
    dato2 = dato1*12
    return jsonify({ "pulgada" : dato2})

@app.route("/pulgada/<string:dato1>")
def get_datosPu(dato1):
    dato = float(dato1)
    return jsonify({ "pulgada" : dato})

@app.route("/pulgadakilo/<string:dato1>")
def get_datosPuK(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.0000254
    return jsonify({ "kilometro" : dato2})

@app.route("/pulgadacenti/<string:dato1>")
def get_datosPuC(dato1):
    dato1 = float(dato1)
    dato2 = dato1*2.54
    return jsonify({ "centimetro" : dato2})

@app.route("/pulgadamilla/<string:dato1>")
def get_datosPuMi(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.000015783
    return jsonify({ "milla" : dato2})

@app.route("/pulgadayarda/<string:dato1>")
def get_datosPuY(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.027777
    return jsonify({ "yarda" : dato2})

@app.route("/pulgadapie/<string:dato1>")
def get_datosPuP(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.083333
    return jsonify({ "pie" : dato2})

@app.route("/pulgadametro/<string:dato1>")
def get_datosPuM(dato1):
    dato1 = float(dato1)
    dato2 = dato1*0.0254
    return jsonify({ "pulgada" : dato2})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
