class Plant:
    def __init__(self, name, species, water_need):
        self.name = name
        self.species = species
        self.water_need = water_need

    def __str__(self):
        return (
            f"Plant(name={self.name}, species={self.species}, "
            f"water_need={self.water_need})"
        )

    def __eq__(self, other):
        if not isinstance(other, Plant):
            return False
        return (
            self.name == other.name
            and self.species == other.species
            and self.water_need == other.water_need
        )


class Sensor:
    def __init__(self, sensor_id, plant_name, humidity):
        self.sensor_id = sensor_id
        self.plant_name = plant_name
        self.humidity = humidity

    def __str__(self):
        return (
            f"Sensor(sensor_id={self.sensor_id}, "
            f"plant_name={self.plant_name}, humidity={self.humidity})"
        )

    def __eq__(self, other):
        if not isinstance(other, Sensor):
            return False
        return (
            self.sensor_id == other.sensor_id
            and self.plant_name == other.plant_name
            and self.humidity == other.humidity
        )


class WateringSchedule:
    def __init__(self, plant_name, hour, water_amount_ml):
        self.plant_name = plant_name
        self.hour = hour
        self.water_amount_ml = water_amount_ml

    def __str__(self):
        return (
            f"WateringSchedule(plant_name={self.plant_name}, "
            f"hour={self.hour}, water_amount_ml={self.water_amount_ml})"
        )

    def __eq__(self, other):
        if not isinstance(other, WateringSchedule):
            return False
        return (
            self.plant_name == other.plant_name
            and self.hour == other.hour
            and self.water_amount_ml == other.water_amount_ml
        )
