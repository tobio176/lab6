# Модель: Чисельне інтегрування методом Симпсона (5 семестр)
# Автор: Тіторага Глєб, група АІ-233

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        x = float(request.args.get('x', 0))
        result = (x ** 3) / 3.0
        
        return jsonify({
            "model": "Метод Симпсона",
            "input_x": x,
            "result": round(result, 4)
        })
    except ValueError:
        return jsonify({"error": "Помилка: параметр 'x' має бути числом"}), 400

if __name__ == '__main__':
    # ЛР7: Вимкнено debug mode, порт береться зі змінної середовища (Render сам його задасть)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
