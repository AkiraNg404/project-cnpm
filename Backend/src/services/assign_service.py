from src.models.assignment import Assignment

class AssignService:
    def __init__(self):
        self.assignments = []

    def is_duplicate(self, paper_id, reviewer_id):
        for a in self.assignments:
            if a.paper_id == paper_id and a.reviewer_id == reviewer_id:
                return True
        return False

    def count_reviewer_papers(self, reviewer_id):
        count = 0
        for a in self.assignments:
            if a.reviewer_id == reviewer_id:
                count += 1
        return count

    def assign_paper(self, paper_id, reviewer):
        if self.is_duplicate(paper_id, reviewer.id):
            return "Paper đã được assign cho reviewer này"

        if self.count_reviewer_papers(reviewer.id) >= reviewer.max_papers:
            return "Reviewer đã đạt giới hạn paper"

        assignment = Assignment(
            len(self.assignments) + 1,
            paper_id,
            reviewer.id
        )
        self.assignments.append(assignment)

        return "Assign paper thành công"
