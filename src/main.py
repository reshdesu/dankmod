#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sims4.commands


# This is just a Hello World script, you can play around with it, do a test compile/decompile/debug, or just delete it
# and start from scratch. The world is yours.


@sims4.commands.Command('everythingisfine', command_type=sims4.commands.CommandType.Live)
def _everythingisfine(_connection=None):
    from datetime import datetime
    # classes
    # override the default output with a better output
    # inspired by loguru
    class DankOutput:
        # init method or constructor
        def __init__(self, _connection=None):
            import inspect
            self.output = sims4.commands.CheatOutput(_connection)

        def info(self, message: str, _connection=None):
            now = datetime.now()
            return self.output(f"[{now}]INFO| {message}")

    class DankHelpers:
        # init method or constructor
        def __init__(self, _connection=None):
            self.output = DankOutput(_connection)

        # helper functions
        def append_command(self, prefix: str, values: list) -> list:
            # TODO: need to use this logic to improve logging
            """import inspect
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            info = ('caller name:' + calframe[1][3])
            self.output.info(info)"""
            # initialize new list to return
            new_list = []
            for idx, value in enumerate(values):
                append_val = prefix + " " + value
                # self.output.info(f"{idx + 1}. {append_val}")
                new_list.append(append_val)
            return new_list

    # initialize class objects
    output = DankOutput(_connection)
    helpers = DankHelpers(_connection)
    # main code
    output.info("Making you DANK! <3")
    # list of cc for making everything fine
    cheats_cc = ['testingcheats true']
    qol_cc = ['household.autopay_bills true', 'bb.showhiddenobjects', 'bb.enablefreebuild',
              'bb.ignoregameplayunlocksentitlemen', 'objects.consumables_infinite_toggle']
    wealth_cc = ['money 500000', 'sims.give_satisfaction_points 50000']
    death_cc = ['death.toggle false']
    traits = ['Antiseptic', 'Business_Savvy', 'Carefree', 'Collector', 'EternalBond', 'Connections',
              'CreativeVisionary', 'CreativelyGifted', 'FamilySim', 'Entrepreneurial', 'EssenceOfFlavor',
              'Expressionistic', 'FreeServices', 'FreshChef', 'Frugal', 'GreatKisser', 'Gregarious', 'GymRat',
              'TheKnack', 'High_Metabolism', 'Hilarious', 'trait_Independent', 'Longevity', 'Marketable', 'Mastermind',
              'Memorable', 'MentallyGifted', 'Mentor', 'MorningPerson', 'Muser', 'OneWithNature', 'NeverWeary',
              'HardlyHungry', 'trait_NightOwl', 'Observant', 'PerfectHost', 'PhysicallyGifted', 'Piper', 'EpicPoet',
              'PotionMaster', 'Chronicler', 'Quick_Learner', 'Savant', 'Shameless', 'Invested', 'Sincere',
              'SociallyGifted', 'SpeedCleaner', 'SpeedReader', 'SteelBladder', 'SuperGreenThumb', 'ValuedCustomer',
              'LivingVicariously', 'Webmaster', 'top_notch_toddler', 'happy_toddler', 'IncrediblyFriendly',
              'StovesAndGrillsMaster', 'Sickness', 'HomeTurf', 'SpiceHound', 'InTheKnow', 'ChopstickSavvy',
              'trait_hidden_career_critic_thrifty']
    traits_cc = helpers.append_command('traits.equip_trait', traits)
    skills = ['Major_Handiness 10', 'Major_Charisma 10', 'Major_Logic 10']
    skills_cc = helpers.append_command('stats.set_skill_level', skills)
    # combine all cc lists
    list_cc = cheats_cc + qol_cc + wealth_cc + death_cc + traits_cc + skills_cc
    # make it rain!
    for cc in list_cc:
        # check what commands were ran
        # output.info(cc)
        sims4.commands.execute(cc, _connection)
    output.info("Your sim is NOW DANK! <3")