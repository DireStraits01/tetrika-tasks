import time


def appearance(intervals):
    puptimes = dc['pupil'][:]
    tuttimes = dc['tutor'][:]
    pupil_in = False
    tutor_in = False

    last = 0
    together = 0
    while puptimes and tuttimes:
        # Pick the event to come next.
        if puptimes[0] < tuttimes[0]:
            evt = puptimes.pop(0)
            pupil_in = not pupil_in
        else:
            evt = tuttimes.pop(0)
            tutor_in = not tutor_in

        tc = time.ctime(evt)
        if pupil_in and tutor_in:
            print( tc, "Both are in the room." )
            last = evt
        else:
            if last:
                print( tc, "No longer both in, together time =", evt-last )
                together += evt-last

            if pupil_in:
                print( tc, "Pupil is in the room alone" )
            elif tutor_in:
                print( tc, "Tutor is in the room alone" )
            else:
                print( tc, "Room is empty" )

    return together

dc = {
      'lesson': [1594663200, 1594666800],
      'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
      'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
print(appearance(dc))