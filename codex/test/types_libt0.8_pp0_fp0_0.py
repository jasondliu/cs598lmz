import types
types.InspectionData = InspectionData
types.MotorcycleTest = MotorcycleTest
types.Inspection = Inspection
types.Inspector = Inspector
types.Station = Station
types.Motorcycle = Motorcycle
types.Motor = Motor

class InspectionDataModel:
    def __init__(self, db):
        self.db = db

    def get_inspection_data(self):
        response = []
        data = {}
        inspection_data = self.db.query(InspectionData).all()
        for data in inspection_data:
            response.append(data.as_dict())
        return response

    def add_inspection_data(self, inspection_data_request):
        try:
            data = InspectionData(
                inspection_type=inspection_data_request.inspection_type,
                description=inspection_data_request.description
            )
            self.db.add(data)
            self.db.commit()

            return data.as_dict()
        except Exception as e:
            return e

