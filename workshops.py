from flask import Blueprint, render_template

workshops_bp = Blueprint("workshops", __name__)

@workshops_bp.route("/workshop/<int:id>")
def workshop_page(id):
    return render_template(f"workshop{id}.html")
