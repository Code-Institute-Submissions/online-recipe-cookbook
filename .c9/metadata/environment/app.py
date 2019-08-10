{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":67,"position":67,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":10,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())",""],"id":7},{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":42},"action":"remove","lines":["task_manager"],"id":8},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["o"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["n"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["l"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["i"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["n"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["e"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["-"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["r"],"id":9},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["e"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["c"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["i"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["p"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":["e"],"id":10},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["p"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["i"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["c"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["e"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["r"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["-"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["e"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["n"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["i"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["l"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["n"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["o"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["c"],"id":11},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["o"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["o"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["k"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["b"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["o"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":37},"action":"remove","lines":["cookboo"],"id":12},{"start":{"row":6,"column":29},"end":{"row":6,"column":31},"action":"remove","lines":["''"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":[";"],"id":13}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":[";"],"id":14}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":31},"action":"insert","lines":["''"],"id":15}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["c"],"id":16},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["o"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["o"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["k"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["b"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["o"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["o"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["k"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["D"]}],[{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["b"],"id":17}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'cookbookDb'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":18},{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":42},"action":"remove","lines":["task_manager"],"id":19},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["c"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["o"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["o"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["k"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["b"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["o"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["o"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["k"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["D"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["b"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":33},"action":"remove","lines":["tasks"],"id":20},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["i"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["n"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["d"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["x"],"id":21}],[{"start":{"row":15,"column":39},"end":{"row":15,"column":68},"action":"remove","lines":[", tasks=mongo.db.tasks.find()"],"id":22}],[{"start":{"row":11,"column":0},"end":{"row":15,"column":40},"action":"remove","lines":["","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"index.html\")"],"id":23},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":24}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":25}],[{"start":{"row":10,"column":0},"end":{"row":13,"column":69},"action":"insert","lines":["@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())"],"id":26}],[{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":33},"action":"remove","lines":["tasks"],"id":28},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["i"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["n"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["d"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["e"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["x"]}],[{"start":{"row":14,"column":40},"end":{"row":14,"column":68},"action":"remove","lines":[" tasks=mongo.db.tasks.find()"],"id":29},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"remove","lines":[","]}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":22},"action":"remove","lines":["get_tasks"],"id":30},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["g"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["e"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["t"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["-"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"remove","lines":["-"],"id":31}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["_"],"id":32}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["t"],"id":33},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["o"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["p"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["_"],"id":34},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["r"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["c"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["i"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["p"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["e"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":13},"action":"remove","lines":["get_tasks"],"id":35},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["g"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["e"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["t"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["_"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["o"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["_"],"id":36}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":12},"action":"remove","lines":["get_top_"],"id":37},{"start":{"row":13,"column":4},"end":{"row":13,"column":19},"action":"insert","lines":["get_top_recipes"]}],[{"start":{"row":14,"column":40},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":33},"action":"remove","lines":["index"],"id":39},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["h"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["o"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["m"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":[","],"id":40}],[{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":[" "],"id":41},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["r"]},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["e"]},{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"insert","lines":["c"]}],[{"start":{"row":14,"column":43},"end":{"row":14,"column":44},"action":"insert","lines":["i"],"id":42},{"start":{"row":14,"column":44},"end":{"row":14,"column":45},"action":"insert","lines":["p"]},{"start":{"row":14,"column":45},"end":{"row":14,"column":46},"action":"insert","lines":["e"]},{"start":{"row":14,"column":46},"end":{"row":14,"column":47},"action":"insert","lines":["s"]},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"insert","lines":[" "],"id":43},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"insert","lines":["m"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":["o"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["n"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":["g"]}],[{"start":{"row":14,"column":49},"end":{"row":14,"column":53},"action":"remove","lines":["mong"],"id":44},{"start":{"row":14,"column":49},"end":{"row":14,"column":54},"action":"insert","lines":["mongo"]}],[{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"insert","lines":["."],"id":45}],[{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"insert","lines":["r"],"id":46},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"insert","lines":["e"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":["c"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["i"]}],[{"start":{"row":14,"column":55},"end":{"row":14,"column":59},"action":"remove","lines":["reci"],"id":47},{"start":{"row":14,"column":55},"end":{"row":14,"column":62},"action":"insert","lines":["recipes"]}],[{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"insert","lines":["."],"id":48}],[{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"insert","lines":["f"],"id":49},{"start":{"row":14,"column":64},"end":{"row":14,"column":65},"action":"insert","lines":["i"]},{"start":{"row":14,"column":65},"end":{"row":14,"column":66},"action":"insert","lines":["n"]},{"start":{"row":14,"column":66},"end":{"row":14,"column":67},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":67},"end":{"row":14,"column":69},"action":"insert","lines":["()"],"id":50}],[{"start":{"row":14,"column":68},"end":{"row":14,"column":69},"action":"remove","lines":[")"],"id":51},{"start":{"row":14,"column":67},"end":{"row":14,"column":69},"action":"remove","lines":["()"]},{"start":{"row":14,"column":66},"end":{"row":14,"column":67},"action":"remove","lines":["d"]},{"start":{"row":14,"column":65},"end":{"row":14,"column":66},"action":"remove","lines":["n"]},{"start":{"row":14,"column":64},"end":{"row":14,"column":65},"action":"remove","lines":["i"]},{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"remove","lines":["f"]},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"remove","lines":["."]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"remove","lines":["s"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["e"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["p"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":["i"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"remove","lines":["c"]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"remove","lines":["e"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"insert","lines":["d"],"id":52},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"insert","lines":["b"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":["."]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["r"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":["s"],"id":53}],[{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["s"],"id":54}],[{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":["c"],"id":55},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"insert","lines":["i"]},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"insert","lines":["p"]},{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"insert","lines":["e"]},{"start":{"row":14,"column":64},"end":{"row":14,"column":65},"action":"insert","lines":["s"]},{"start":{"row":14,"column":65},"end":{"row":14,"column":66},"action":"insert","lines":["."]},{"start":{"row":14,"column":66},"end":{"row":14,"column":67},"action":"insert","lines":["f"]},{"start":{"row":14,"column":67},"end":{"row":14,"column":68},"action":"insert","lines":["i"]},{"start":{"row":14,"column":68},"end":{"row":14,"column":69},"action":"insert","lines":["n"]},{"start":{"row":14,"column":69},"end":{"row":14,"column":70},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":70},"end":{"row":14,"column":72},"action":"insert","lines":["()"],"id":56}],[{"start":{"row":14,"column":72},"end":{"row":14,"column":73},"action":"insert","lines":[")"],"id":57}],[{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"remove","lines":[" "],"id":58}],[{"start":{"row":7,"column":71},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":1},"end":{"row":8,"column":3},"action":"insert","lines":["\"\""],"id":60}],[{"start":{"row":8,"column":2},"end":{"row":8,"column":110},"action":"insert","lines":["mongodb+srv://root-user96:r00tUser96@myfirstcluster-ehz2d.mongodb.net/cookbookDb?retryWrites=true&w=majority"],"id":61}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["A"],"id":62}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["A"],"id":63}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["a"],"id":64},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["p"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["p"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["."]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["c"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["n"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["f"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["i"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["["],"id":65},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["]"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["\"\""],"id":66}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["M"],"id":67},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["O"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":14},"action":"remove","lines":["MO"],"id":68},{"start":{"row":8,"column":12},"end":{"row":8,"column":21},"action":"insert","lines":["MONGO_URI"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["/"],"id":69},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["/"]}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":["/"],"id":70},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["/"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"],"id":71}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":134},"action":"remove","lines":["app.config[\"MONGO_URI\"]=\"mongodb+srv://root-user96:r00tUser96@myfirstcluster-ehz2d.mongodb.net/cookbookDb?retryWrites=true&w=majority\""],"id":72}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["#"],"id":73}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":71},"end":{"row":7,"column":71},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565439500830,"hash":"1aeadb21debb4b41f294eb5b3f94e1eb9e3a431f"}