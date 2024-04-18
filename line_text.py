class LineText:
    def __init__(self, data: str, procedencia: int):
        self.data = data
        self.procedencia = procedencia

    def __str__(self):
        result = ""
        result += str(self.data)
        result += " "
        result += str(self.procedencia)
        return result
