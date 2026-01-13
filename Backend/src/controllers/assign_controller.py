from src.services.assign_service import AssignService
from src.models.reviewer import Reviewer

assign_service = AssignService()

def assign_paper_controller(paper_id, reviewer_id):
    reviewer = Reviewer(reviewer_id, "Reviewer demo", 3)
    return assign_service.assign_paper(paper_id, reviewer)
