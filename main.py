import playsound 
import os

class SCPSounds:
    sounds = {}

    def __init__(self):
        pass

    def get_sounds(self, path: str) -> bool:
        try:
            files = os.listdir(path)
            for i in files:
                split = i.split('.')
                sound_name = split[0].removeprefix('_')
                try:
                    if split[1] != 'wav' and split[1] != 'mp3':
                        continue
                    self.sounds[sound_name] = f'{path}/{i}'
                except IndexError:
                    continue
            if len(self.sounds) == 0:
                print(f'No wav or mp3 sounds detected.')
                return False
            print(f'Got {len(files)} sounds.')
            return True
        except FileNotFoundError:
            print('Folder not found.')
            return False
        except NotADirectoryError:
            print('Given path is not a directory.')
            return False

    def play_sound(self, phrase: str):
        words = phrase.split(' ')
        for i in words:
            if i not in self.sounds:
                print(f'WARN: sound "{i}" not found, skipping...')
                continue
            playsound.playsound(self.sounds[i])

def main():
    scp = SCPSounds()
    path = input('Enter sounds dir absolute path: ')
    if scp.get_sounds(path) == False:
        return
    phrase = input('Enter sound names (split them by space): ')
    scp.play_sound(phrase)

if __name__ == '__main__':
    main()