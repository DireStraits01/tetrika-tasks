
def appearance(intervals):
    lesson_times = dc['lesson']
    pupil_times = dc['pupil']
    tutor_times = dc['tutor']
    total_time_pupil = 0
    start_time_pupil = 0
    end_time_pupil = 0

    if len(pupil_times) > len(tutor_times):
        for index, times in pupil_times

    for index, time in enumerate(pupil_times):
        if (index % 2) == 0:
           start_time_pupil = time
        else:
            end_time_pupil = time

        if start_time_pupil != 0 and end_time_pupil !=0:
            total_time_pupil += (end_time_pupil - start_time_pupil)
            start_time_pupil = 0
            end_time_pupil = 0

    tutor_times = dc['tutor']
    total_time_tutor = 0
    start_time_tutor = 0
    end_time_tutor = 0
    for index, time in enumerate(tutor_times):
        if (index % 2) == 0:
            start_time_tutor = time
        else:
            end_time_tutor = time

        if start_time_tutor != 0 and end_time_tutor != 0:
            total_time_tutor += (end_time_tutor - start_time_tutor)
            start_time_tutor = 0
            end_time_tutor = 0
    return total_time_tutor + total_time_pupil


dc = {
  'lesson': [1594663200, 1594666800],
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
print(appearance(dc))

