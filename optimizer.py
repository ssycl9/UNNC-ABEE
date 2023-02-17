from typing import List, Tuple
from simulation import Simulation


class Optimizer:
    def obtain(self, simulation: Simulation, parameter_ranges: List[Tuple[float, float]]):
        self.simulation = simulation
        self.parameter_ranges = parameter_ranges

    def _generate_idf(self, parameter_values: List[float]) -> str:
        with open("1ZoneUncontrolled_win_test_template.idf") as f:
            template = f.read()
        for i, parameter_value in enumerate(parameter_values):
            template = template.replace(f"PARAMETER_{i+1}", str(parameter_value))
        with open("1ZoneUncontrolled_win_test.idf", "w") as f:
            f.write(template)
        return "1ZoneUncontrolled_win_test.idf"

    def _run_simulation(self, parameter_values: List[float]) -> float:
        idf_file_path = self._generate_idf(parameter_values)
        return self.simulation.run()

    def optimize(self) -> List[float]:
        parameter_values = [(p[0] + p[1]) / 2 for p in self.parameter_ranges]
        step_size = max([(p[1] - p[0]) / 10 for p in self.parameter_ranges])
        while step_size > 0.001:
            values_to_evaluate = []
            for i, parameter_value in enumerate(parameter_values):
                for offset in [-1, 0, 1]:
                    if offset == 0:
                        continue
                    new_value = parameter_value + offset * step_size
                    if new_value < self.parameter_ranges[i][0] or new_value > self.parameter_ranges[i][1]:
                        continue
                    values_to_evaluate.append(
                        parameter_values[:i] + [new_value] + parameter_values[i+1:]
                    )
            results = [self._run_simulation(v) for v in values_to_evaluate]
            best_result = max(results)
            best_index = results.index(best_result)
            parameter_values = values_to_evaluate[best_index]
            step_size /= 2
        return parameter_values
