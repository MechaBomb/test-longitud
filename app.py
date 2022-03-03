from flask import Flask, jsonify, request

app = Flask(__name__)

#Conversiones a metro

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

@app.route("/metromili/<string:dato1>")
def get_datosMMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1000
	return jsonify({ "milimetro" : dato2})

@app.route("/metrolegua/<string:dato1>")
def get_datosML(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.0002071
	return jsonify({ "legua" : dato2})

@app.route("/metromillan/<string:dato1>")
def get_datosMMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.0005399
	return jsonify({ "milla nautica" : dato2})

#Conversiones a kilómetro

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

@app.route("/kilomili/<string:dato1>")
def get_datosKMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1000000
	return jsonify({ "milimetro" : dato2})

@app.route("/kilolegua/<string:dato1>")
def get_datosKL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.2071237
	return jsonify({ "legua" : dato2})

@app.route("/kilomillan/<string:dato1>")
def get_datosKMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.5399568
	return jsonify({ "milla nautica" : dato2})

#Conversiones a centímetro

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

@app.route("/centimili/<string:dato1>")
def get_datosCMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*10
	return jsonify({ "milimetro" : dato2})

@app.route("/centilegua/<string:dato1>")
def get_datosCL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.000002071
	return jsonify({ "legua" : dato2})

@app.route("/centimillan/<string:dato1>")
def get_datosCMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.000005399
	return jsonify({ "milla nautica" : dato2})

#Conversiones a milla

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

@app.route("/millamili/<string:dato1>")
def get_datosMiMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1609344
	return jsonify({ "milimetro" : dato2})

@app.route("/millalegua/<string:dato1>")
def get_datosMiL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.3333333
	return jsonify({ "legua" : dato2})

@app.route("/millamillan/<string:dato1>")
def get_datosMiMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.8689762
	return jsonify({ "milla nautica" : dato2})

#Conversiones a yarda

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

@app.route("/yardamili/<string:dato1>")
def get_datosYMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*914.4
	return jsonify({ "milimetro" : dato2})

@app.route("/yardalegua/<string:dato1>")
def get_datosYL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00018939
	return jsonify({ "legua" : dato2})

@app.route("/yardamillan/<string:dato1>")
def get_datosYMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00049374
	return jsonify({ "milla nautica" : dato2})

#Conversiones a pie

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

@app.route("/piemili/<string:dato1>")
def get_datosPMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*304.8
	return jsonify({ "milimetro" : dato2})

@app.route("/pielegua/<string:dato1>")
def get_datosPL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00006313
	return jsonify({ "legua" : dato2})

@app.route("/piemillan/<string:dato1>")
def get_datosPMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00016458
	return jsonify({ "milla nautica" : dato2})

#Conversiones a pulgada

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

@app.route("/pulgadamili/<string:dato1>")
def get_datosPuMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*25.4
	return jsonify({ "milimetro" : dato2})

@app.route("/pulgadalegua/<string:dato1>")
def get_datosPuL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00000526
	return jsonify({ "legua" : dato2})

@app.route("/pulgadamillan/<string:dato1>")
def get_datosPuMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00001371
	return jsonify({ "milla nautica" : dato2})

#Conversiones a milimetro

@app.route("/mili/<string:dato1>")
def get_datosMm(dato1):
	dato = float(dato1)
	return jsonify({ "milimetro" : dato})

@app.route("/milimetro/<string:dato1>")
def get_datosMmM(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.001
	return jsonify({ "metro" : dato2})

@app.route("/milikilo/<string:dato1>")
def get_datosMmK(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.000001
	return jsonify({ "kilometro" : dato2})

@app.route("/milicenti/<string:dato1>")
def get_datosMmC(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.1
	return jsonify({ "centimetro" : dato2})

@app.route("/milimilla/<string:dato1>")
def get_datosMmMi(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00000062137119
	return jsonify({ "milla" : dato2})

@app.route("/miliyarda/<string:dato1>")
def get_datosMmY(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00109361
	return jsonify({ "yarda" : dato2})

@app.route("/milipie/<string:dato1>")
def get_datosMmP(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00328084
	return jsonify({ "pie" : dato2})

@app.route("/milipulgada/<string:dato1>")
def get_datosMmPu(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.03937008
	return jsonify({ "milimetro" : dato2})

@app.route("/mililegua/<string:dato1>")
def get_datosMmL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.00000020712373
	return jsonify({ "legua" : dato2})

@app.route("/milimillan/<string:dato1>")
def get_datosMmMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.0000005399568
	return jsonify({ "milla nautica" : dato2})

#Conversiones a legua

@app.route("/legua/<string:dato1>")
def get_datosL(dato1):
	dato = float(dato1)
	return jsonify({ "legua" : dato})

@app.route("/leguametro/<string:dato1>")
def get_datosLM(dato1):
	dato1 = float(dato1)
	dato2 = dato1*4828.032
	return jsonify({ "metro" : dato2})

@app.route("/leguakilo/<string:dato1>")
def get_datosLK(dato1):
	dato1 = float(dato1)
	dato2 = dato1*4.828032
	return jsonify({ "kilometro" : dato2})

@app.route("/leguacenti/<string:dato1>")
def get_datosLC(dato1):
	dato1 = float(dato1)
	dato2 = dato1*482803.2
	return jsonify({ "centimetro" : dato2})

@app.route("/leguamilla/<string:dato1>")
def get_datosLMi(dato1):
	dato1 = float(dato1)
	dato2 = dato1*3
	return jsonify({ "milla" : dato2})

@app.route("/leguayarda/<string:dato1>")
def get_datosLY(dato1):
	dato1 = float(dato1)
	dato2 = dato1*5280
	return jsonify({ "yarda" : dato2})

@app.route("/leguapie/<string:dato1>")
def get_datosLP(dato1):
	dato1 = float(dato1)
	dato2 = dato1*15840
	return jsonify({ "pie" : dato2})

@app.route("/leguapulgada/<string:dato1>")
def get_datosLPu(dato1):
	dato1 = float(dato1)
	dato2 = dato1*190080
	return jsonify({ "pulgada" : dato2})

@app.route("/leguamili/<string:dato1>")
def get_datosLMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*4828032
	return jsonify({ "milimetro" : dato2})

@app.route("/leguamillan/<string:dato1>")
def get_datosLMn(dato1):
	dato1 = float(dato1)
	dato2 = dato1*2.6069287
	return jsonify({ "milla nautica" : dato2})

#Conversiones a milla nautica

@app.route("/millan/<string:dato1>")
def get_datosMn(dato1):
	dato = float(dato1)
	return jsonify({ "milla nautica" : dato})

@app.route("/millanmetro/<string:dato1>")
def get_datosMnM(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1852
	return jsonify({ "metro" : dato2})

@app.route("/millankilo/<string:dato1>")
def get_datosMnK(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1.852
	return jsonify({ "kilometro" : dato2})

@app.route("/millancenti/<string:dato1>")
def get_datosMnC(dato1):
	dato1 = float(dato1)
	dato2 = dato1*185200
	return jsonify({ "centimetro" : dato2})

@app.route("/millanmilla/<string:dato1>")
def get_datosMnMi(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1.3835
	return jsonify({ "milla" : dato2})

@app.route("/millanyarda/<string:dato1>")
def get_datosMnY(dato1):
	dato1 = float(dato1)
	dato2 = dato1*2025.3718285
	return jsonify({ "yarda" : dato2})

@app.route("/millanpie/<string:dato1>")
def get_datosMnP(dato1):
	dato1 = float(dato1)
	dato2 = dato1*6076.1154856
	return jsonify({ "pie" : dato2})

@app.route("/millanpulgada/<string:dato1>")
def get_datosMnPu(dato1):
	dato1 = float(dato1)
	dato2 = dato1*72913.385827
	return jsonify({ "pulgada" : dato2})

@app.route("/millanmili/<string:dato1>")
def get_datosMnMm(dato1):
	dato1 = float(dato1)
	dato2 = dato1*1852000
	return jsonify({ "milimetro" : dato2})

@app.route("/millanlegua/<string:dato1>")
def get_datosMnL(dato1):
	dato1 = float(dato1)
	dato2 = dato1*0.3835931
	return jsonify({ "legua" : dato2})

#Condicional

if __name__ == '__main__':
	app.run(debug=True, port=5000)
