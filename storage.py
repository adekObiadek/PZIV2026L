from models import Plant, Sensor, WateringSchedule


def create_initial_data():
    return {
        "plant_1": Plant("Monstera", "Monstera deliciosa", "medium"),
        "plant_2": Plant("Fikus", "Ficus elastica", "low"),
        "plant_3": Plant("Paproc", "Nephrolepis exaltata", "high"),
        "plant_4": Plant("Aloes", "Aloe vera", "low"),
        "sensor_1": Sensor("S001", "Monstera", 42),
        "sensor_2": Sensor("S002", "Fikus", 55),
        "sensor_3": Sensor("S003", "Paproc", 31),
        "sensor_4": Sensor("S004", "Aloes", 68),
        "schedule_1": WateringSchedule("Monstera", "08:00", 250),
        "schedule_2": WateringSchedule("Fikus", "09:30", 150),
        "schedule_3": WateringSchedule("Paproc", "07:15", 300),
        "schedule_4": WateringSchedule("Aloes", "18:00", 100),
    }


def get_objects_by_class(data, class_name):
    return [
        item
        for item in data.values()
        if item.__class__.__name__ == class_name
    ]
