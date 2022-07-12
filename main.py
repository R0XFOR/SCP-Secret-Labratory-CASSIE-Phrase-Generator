from time import sleep
import playsound
import os

class SCPSounds:
    sounds = {}

    def __init__(self) -> None:
        pass

    def get_sounds(self, path: str) -> bool:
        try:
            files = os.listdir(path)
            for i in files:
                split = i.split('.')
                if len(split) < 2 or split[1] != 'wav' and split[1] != 'mp3':
                    continue
                sound_name = split[0].removeprefix('_')
                self.sounds[sound_name] = f'{path}/{i}'
            sounds_cound = len(self.sounds)
            if sounds_cound == 0:
                print(f'No wav or mp3 sounds detected.')
                return False
            print(f'Got {sounds_cound} sounds.')
            return True
        except FileNotFoundError:
            print('FATAL: folder not found.')
            return False
        except NotADirectoryError:
            print('FATAL: given path is not a directory.')
            return False
    
    def word_play(self, word: str):
        clean_word = word.lower().removesuffix('.').removesuffix(',')
        word_suffix = word[-1] if word[-1] == '.' or word[-1] == ',' else ''
        if len(clean_word) != 0:
            if clean_word not in self.sounds:
                print(f'WARN: sound "{clean_word}" not found, skipping...')
            else:
                print(f'INFO: playing sound "{clean_word}" with file path "{self.sounds[clean_word]}"')
                playsound.playsound(self.sounds[clean_word])
        if word_suffix == '.':
            print('INFO: found dot, sleeping for 0.5 seconds.')
            sleep(0.5)
        elif word_suffix == ',':
            print('INFO: found comma, sleeping for 0.2 seconds.')
            sleep(0.2)
            

    def play_sounds(self, phrase: str) -> None:
        words = phrase.split()
        for i in words:
            self.word_play(i)

def main():
    scp = SCPSounds()
    path = input('Enter sounds dir absolute path: ')
    if scp.get_sounds(path) == False:
        return
    phrase = input('Enter sound names (split them by space): ')
    scp.play_sounds(phrase)

if __name__ == '__main__':
    main()
