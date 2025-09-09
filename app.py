from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculate():
    try:
        net_income = float(request.args.get("net_income", 0))
        salary = request.args.get("salary", None)
        admin_costs = float(request.args.get("admin_costs", 1200))

        if not salary:
            salary = net_income * 0.80
        else:
            salary = float(salary)

        SE_TAX_RATE = 0.153
        distribution = net_income - salary
        sole_prop_se_tax = net_income * SE_TAX_RATE
        s_corp_se_tax = salary * SE_TAX_RATE
        tax_savings = sole_prop_se_tax - s_corp_se_tax
        net_benefit = tax_savings - admin_costs
        roi = (net_benefit / admin_costs) * 100 if admin_costs else 0

        return jsonify({
            "net_income": net_income,
            "salary": round(salary, 2),
            "distribution": round(distribution, 2),
            "sole_prop_se_tax": round(sole_prop_se_tax, 2),
            "s_corp_se_tax": round(s_corp_se_tax, 2),
            "admin_costs": admin_costs,
            "tax_savings": round(tax_savings, 2),
            "net_benefit": round(net_benefit, 2),
            "roi_percent": round(roi, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()
