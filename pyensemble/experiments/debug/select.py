# select.py

from django.conf import settings
from pyensemble.models import Stimulus

import os, random
import pdb


def select_audio(request, *args, **kwargs):
    name = kwargs.get('name', None)
    playlist = kwargs.get('playlist', None)
    use_jspsych = kwargs.get('use_jspsych', True)

    stimulus = None
    timeline = []
    # Fetch the stimulus object if we are giving a name
    if name:
        stimulus = Stimulus.objects.get(name=name)

    # Select a stimulus at random from a playlist if specified
    if not stimulus and playlist:
        stimuli = Stimulus.objects.filter(playlist=playlist, file_format='.mp3')

        # Select one at random
        if stimuli.count():
            stimidx = random.randrange(0, stimuli.count())
            stimulus = stimuli[stimidx]

    if stimulus and use_jspsych:
        if settings.USE_AWS_STORAGE:
            stimulus_url = stimulus.location.url
        else:
            stimulus_url = os.path.join(settings.MEDIA_URL, stimulus.location.url)

        trial = {
            'type': 'audio-keyboard-response',
            'stimulus': stimulus_url,
            'choices': 'none',
            'click_to_start': True,
            'trial_ends_after_audio': True,
            'trial_duration': 3000,
        }

        if trial['click_to_start']:
            trial['prompt'] = '<a id="start_button" class="btn btn-primary" role="button"  href="#">Start sound</a>'

        trial_welcome = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': "Welcome to the experiment. Press any key to begin.",
        }

        #       trial_instructions = {
        #           'type': 'jsPsychHtmlKeyboardResponse',
        #           'stimulus': `
        #   <p>In this experiment, a pair of letters will appear in the center
        #   of the screen, one after the other.</p>
        #   <p>If you see the sequence <strong>A-X</strong>,
        #   press the letter J on the keyboard as fast as you can.</p>
        #   <p>For any other letter sequence, press the letter F.</p>
        #   <p>Press any key to begin.</p>
        # `,
        #           post_trial_gap: 2000
        #       }

        trial_fixation = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': '<div style="font-size:60px;">+</div>',
            'choices': 'NO_KEYS',
            'trial_duration': 250,
            'post_trial_gap': 750,
        }

        trial_cue = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': jsPsych.timelineVariable('cue_stimulus'),
            'choices': 'NO_KEYS',
            'trial_duration': 250,
            'post_trial_gap': 750,
        }

        trial_probe = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': jsPsych.timelineVariable('probe_stimulus'),
            'choices': 'NO_KEYS',
            'trial_duration': 250,
            'post_trial_gap': 750,
        }

        trial_response = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': '<div style="font-size:60px;">+</div>',
            'choices': ['f', 'j'],
        }

        trial_slow_response_feedback = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': '',
            'choices': 'NO_KEYS',
        }

        trial_short_break = {
            'type': 'jsPsychVideoKeyboardResponse',
            'stimulus': ['vid\Video effort attribution 1080p.mp4'],
            'prompt': '<p>Take a break! Press any key when you are ready to continue.</p>',
            'width': 800,
            'height': 450,
            'autoplay': true,
            'controls': false,
            'trial_ends_after_video': false,
            'choices': 'ALL_KEYS'
        }

        trial_long_break = {
            'type': 'jsPsychHtmlKeyboardResponse',
            'stimulus': '<p>You may take a 2-minute break. Press any key when you are ready to continue.</p>',
            'trial_duration': 120000,
        }

        # trial_test_procedure = {
        #     'type': 'with-replacement',
        #     'size': 1,
        #     'weights': [70, 10, 10, 10],
        # }

      #   trial_debrief_block = {
      #       'type': 'jsPsychHtmlKeyboardResponse',
      #       'stimulus': function() {
      #
      #           var trials = jsPsych.data.get().filter({
      #               task: 'response'
      #           }); // filtering data where task is 'response'
      #           var correct_trials = trials.filter({
      #               correct: true
      #           });
      #           var accuracy = Math.round(correct_trials.count() / trials.count() * 100);
      #           var rt = Math.round(correct_trials.select('rt').mean());
      #
      #           return `<p>You responded correctly on ${accuracy}% of the trials.</p>
      # <p>Your average response time was ${rt}ms.</p>
      # <p>Press any key to complete the experiment. Thank you!</p>`;
      #   }

        timeline.append(trial)
        timeline.append(trial_welcome)
        timeline.append(trial_fixation)
        timeline.append(trial_cue)
        timeline.append(trial_fixation)
        timeline.append(trial_probe,)
        timeline.append(trial_response)
        timeline.append(trial_slow_response_feedback)


    stimulus_id = None
    if stimulus:
        stimulus_id = stimulus.id

    return timeline, stimulus_id
