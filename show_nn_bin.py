#!/usr/bin/env python3
import sys

import numpy as np

STANDARD_ARCHITECTURE = (
    "Features=HalfKP(Friend)[125388->256x2],"
    + "Network=AffineTransform[1<-32](ClippedReLU[32](AffineTransform[32<-32]("
    + "ClippedReLU[32](AffineTransform[32<-512](InputSlice[512(0:512)])))))"
)


def show(f):
    version = int.from_bytes(f.read(4), "little")
    hash_val = int.from_bytes(f.read(4), "little")
    architecture_size = int.from_bytes(f.read(4), "little")
    architecture = f.read(architecture_size).decode()
    header = int.from_bytes(f.read(4), "little")

    print(f"{hex(version) = }")
    print(f"{hex(hash_val) = }")
    print(f"{architecture_size = }")
    print(f"{architecture = }")
    print(f"{hex(header) = }")

    if architecture != STANDARD_ARCHITECTURE:
        print("not standard NNUE.")
        return
    else:
        print("---- standard NNUE ----")

    ft_b = np.fromfile(f, dtype="<i2", count=256)
    ft_w = np.fromfile(f, dtype="<i2", count=256 * 81 * 1548)
    header2 = int.from_bytes(f.read(4), "little")
    hl1_b = np.fromfile(f, dtype="<i4", count=32)
    hl1_w = np.fromfile(f, dtype="<i1", count=32 * 512)
    hl2_b = np.fromfile(f, dtype="<i4", count=32)
    hl2_w = np.fromfile(f, dtype="<i1", count=32 * 32)
    ol_b = np.fromfile(f, dtype="<i4", count=1)
    ol_w = np.fromfile(f, dtype="<i1", count=32)

    print(f"{ft_b=}")
    print(f"{ft_w=}")
    print(f"{header2=}")
    print(f"{hl1_b=}")
    print(f"{hl1_w=}")
    print(f"{hl2_b=}")
    print(f"{hl2_w=}")
    print(f"{ol_b=}")
    print(f"{ol_w=}")


def main(argv):
    if len(argv) < 2:
        print("usage: {argv[0]} nn.bin", file=sys.stderr)
        sys.exit(0)
    nn_bin = argv[1]
    print(f"load {nn_bin}")
    with open(nn_bin, "rb") as f:
        show(f)


if __name__ == "__main__":
    main(sys.argv)
