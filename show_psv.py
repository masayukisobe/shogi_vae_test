#!/usr/bin/env python3
import sys

import cshogi
import numpy as np


def show(psfens, _from, _to):
    print(psfens.shape)
    print(psfens[0].dtype)
    _from = max(0, _from)
    _to = min(psfens.shape[0], _to)
    board = cshogi.Board()
    for i in range(_from, _to):
        print(f"----\nrecord No. {i+1}")
        psv = psfens[i]
        board.set_psfen(psv["sfen"])
        sfen = board.sfen()
        ply = psv["gamePly"]
        score = psv["score"]
        result = psv["game_result"]
        move16 = cshogi.move16_from_psv(psv["move"])
        best_move = cshogi.move_to_csa(move16)
        print(f"{sfen=}")
        print(f"{ply=}, {score=}, {result=}, {best_move=}")


def main(argv):
    if len(argv) < 4:
        print(f"usage: {argv[0]} psv.bin from to", file=sys.stderr)
        sys.exit(0)
    psv_bin = argv[1]
    _from = int(argv[2])
    _to = int(argv[3])
    print(f"load {psv_bin}")
    psfens = np.fromfile(psv_bin, dtype=cshogi.PackedSfenValue)
    show(psfens, _from, _to)


if __name__ == "__main__":
    main(sys.argv)
