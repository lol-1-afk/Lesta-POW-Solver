from Crypto.Hash import keccak
from models import Challenge


class LestaPowSolver:
    """
    webpack:///node_modules/wg-riddler/lib/pow.js
    https://pastebin.com/tRETy3yZ
    """

    def __init__(self, challenge: Challenge):
        self.challenge = challenge

    def make_stamp(self) -> str:
        """
        Makes a stamp from challenge
        :return: stamp - string
        :rtype: str
        """

        return ":".join([
            str(self.challenge.algorithm.version),
            str(self.challenge.complexity),
            str(self.challenge.timestamp),
            self.challenge.algorithm.resourse,
            self.challenge.algorithm.extension,
            self.challenge.random_string
        ])

    def make_prefix(self) -> str:
        """
        Makes a prefix from challenge
        :return: prefix - string
        :rtype: str
        """

        return self.challenge.complexity * "0"

    def solve_challenge(self) -> int:
        """
        Solves challenge
        :return: step index (pow)- int
        :rtype: int
        """

        stamp = self.make_stamp()
        prefix = self.make_prefix()
        step = 0

        while True:
            keccak_hash = keccak.new(digest_bits=512)
            keccak_hash.update((":".join([stamp, str(step)])).encode())
            hashed = keccak_hash.hexdigest()

            is_prefix_valid = hashed.startswith(prefix)
            if is_prefix_valid:
                return step

            step += 1
            continue
