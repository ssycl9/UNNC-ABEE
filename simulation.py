import subprocess
import re
from typing import List


class Simulation:
    def simulate(self, idf_file_path: str):
        self.idf_file_path = idf_file_path

    def run(self) -> float:
        result = subprocess.run(
            ["energyplus", "-r", "-x", "-d", "output", self.idf_file_path],
            capture_output=True,
            text=True,
        )
        output = result.stdout
        m = re.search(r"Average.*C  .*GJ", output)
        if not m:
            raise Exception("Failed to parse simulation result")
        return float(m.group().split()[1])
