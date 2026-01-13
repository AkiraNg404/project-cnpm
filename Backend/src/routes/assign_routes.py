from flask import Blueprint, request
from src.controllers.assign_controller import assign_paper_controller

assign_bp = Blueprint("assign", __name__)

@assign_bp.route("/assign", methods=["POST"])
def assign():
    data = request.json
    return assign_paper_controller(
        data["paper_id"],
        data["reviewer_id"]
    )
