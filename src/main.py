from datetime import timedelta, date, datetime;
from pathlib import Path;

from nicegui import ui, app;

SEMESTER_START_DATE = date.fromisoformat('2025-09-08');
SEMESTER_START_WEEK_MONDAY = SEMESTER_START_DATE - timedelta(days=SEMESTER_START_DATE.weekday());
SEMESTER_END_DATE = date.fromisoformat('2026-01-12');
_i = 0;
while True:
    if ( SEMESTER_START_WEEK_MONDAY + timedelta(weeks=_i) ) >= SEMESTER_END_DATE:
        break;
    _i += 1;
MAX_WEEK = _i;



def main():

    today = date.today();
    d_day = (today-SEMESTER_START_WEEK_MONDAY).days;
    week  = (d_day//7)+1;

    odd_or_even = '单周' if week%2 == 1 else '双周';

    with ui.timeline(side='right'):
        ui.timeline_entry(
            '',
            subtitle=f'Week 1 ({SEMESTER_START_DATE})',
            color='gray-700',
        );

        for i in range(2, week):
            ui.timeline_entry(
                '',
                subtitle=f'Week {i}',
                color='gray-800',
            );

        i += 1;
        ui.timeline_entry(
            '',
            title=f'{odd_or_even}',
            subtitle=f'Week {i} (This week)',
            color='blue-400',
            icon='add_task',
        );

        for i in range(week+1, MAX_WEEK):
            ui.timeline_entry(
                '',
                subtitle=f'Week {i}',
                color='green-900',
            );

        ui.timeline_entry(
            '',
            subtitle=f'Week {MAX_WEEK} ({SEMESTER_END_DATE})',
            color='green-900',
        );

    app.native.window_args['resizable'] = False;
    ui.run(
        reload=False,
        dark=True,
        native=True,
        window_size=(320, 880),
    );

if __name__ in {"__main__", "__mp_main__"}:
    main()
