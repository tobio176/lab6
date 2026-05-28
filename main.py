# Модель: Чисельне інтегрування методом Симпсона (5 семестр)
# Автор: Тіторага Глєб, група АІ-233

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    # Отримуємо параметр 'x' через URL (варіант для парного номера). 
    # За замовчуванням беремо 0, якщо параметр не передано.
    try:
        x = float(request.args.get('x', 0))
        
        # Математична модель: спрощене обчислення інтегралу від 0 до x 
        # для функції f(t) = t^2. Аналітичний результат: (x^3) / 3
        result = (x ** 3) / 3.0
        
        return jsonify({
            "model": "Метод Симпсона",
            "input_x": x,
            "result": round(result, 4)
        })
    except ValueError:
        return jsonify({"error": "Помилка: параметр 'x' має бути числом"}), 400

if __name__ == '__main__':
    # Запускаємо сервер на всіх інтерфейсах (0.0.0.0), щоб він був доступний з Docker
    app.run(host='0.0.0.0', port=5000)