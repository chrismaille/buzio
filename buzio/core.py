import os
import subprocess
import sys
import yaml
from shutil import get_terminal_size
from colorama import Fore, Back, Style
from unidecode import unidecode

class Console():

    DEFAULT_THEMES = {
        'box': Fore.LIGHTCYAN_EX,
        'choose': Fore.BLUE,
        'confirm': Fore.LIGHTYELLOW_EX,
        'error': Fore.RED,
        'info': Fore.CYAN,
        'section': Fore.BLUE,
        'success': Fore.GREEN,
        'warning': Fore.YELLOW
    }

    def __init__(self, format_only=False, theme_dict=DEFAULT_THEMES):
        self.format_only = format_only
        self.theme_dict= theme_dict

    def _get_style(self):
        if not isinstance(self.theme_dict, dict):
            raise ValueError("Themes List must be a dictionary.")
        
        return self.theme_dict.get(self.theme, "")

    def _humanize(self, text):
        if isinstance(text, str):
            ret = text
        else:
            data = self.text
            if isinstance(data, bool):
                ret = "Sim" if data else "Não"
            elif isinstance(data, list) or isinstance(data, tuple):
                ret = ", ".join(data)
            elif isinstance(data, dict):
                ret = "\n".join([
                    "{}: {}: {}".format(i + 1, key, data[key])
                    for i, key in enumerate(data)
                ])
            else:
                ret = str(data)

        self.text = ret

    def _print(self):
       
        if self.prefix:
            self.text = "{}: {}".format(self.prefix, self.text)
        
        if self.transform:
            if 'title' in self.transform:
                self.text = self.text.title()
            if 'upper' in self.transform:
                self.text = self.text.upper()
            if 'small' in self.transform:
                self.text = self.text.lower()    
        
        if self.theme:
            self.text = "{}{}{}".format(
                self._get_style(),
                self.text,
                Style.RESET_ALL
            )
        if self.transform and 'bold' in self.transform:
            self.text = "{}{}".format(Style.BRIGHT, self.text)

        if not self.format_only:
            print(self.text)

        return self.text


    def success(self, text, theme="success", transform=None, use_prefix=True, prefix="Success"):
        self._humanize(text)
        self.prefix = prefix if use_prefix else ""
        self.theme = theme
        self.transform = transform
        return self._print()

    def info(self, text, theme="info", transform=None, use_prefix=True, prefix="Info"):
        self._humanize(text)
        self.prefix = prefix if use_prefix else ""
        self.theme = theme
        self.transform = transform
        return self._print()

    def warning(self, text, theme="warning", transform=None, use_prefix=True, prefix="Warning"):
        self._humanize(text)
        self.prefix = prefix if use_prefix else ""
        self.theme = theme
        self.transform = transform
        return self._print()

    def error(self, text, theme="error", transform=None, use_prefix=True, prefix="Error"):
        self._humanize(text)
        self.prefix = prefix if use_prefix else ""
        self.theme = theme
        self.transform = transform
        return self._print()

    def section(self, text, theme="section", transform=None, use_prefix=False, prefix="Section", full_width=False):
        self._humanize()
        if full_width:
            longest_line = get_terminal_size(fallback=(80,24))[0]
        else:
            line_sizes = [
                len(line) + 4
                for line in self.text.split("\n")
            ]
            longest_line = sorted(line_sizes, reverse=True)[0]
        if 'center' in transform:
            format_text = "> {:^{num}} <"
        elif 'right' in transform:
            format_text = " {:>{num}} <<"
        else:
            format_text = ">> {:<{num}} "
        main_lines = [
            format_text.format(line, num=longest_line - 4)
            for line in self.text.split("\n")
        ]
        bottom_line = "{:-^{num}}".format('', num=longest_line)
        self.text = "\n{}{}\n".format(
            "\n".join(main_lines),
            bottom_line
        )
        self.prefix = prefix if use_prefix else ""
        self.theme = theme
        return self._print()

    def box(self, text, theme="box", transform=None):
        self._humanize()
        line_sizes = [
                len(line)
                for line in self.text.split("\n")
            ]
        longest_line = sorted(line_sizes, reverse=True)[0]

        horizontal_line = "{:*^{num}}".format('', num=longest_line + 6)
        vertical_line = "*{:^{num}}*".format('', num=longest_line + 4)

        main_texts = [
            "*{:^{num}}*".format(
                text_line, num=longest_line + 4
            )
            for text_line in text.split("\n")
        ]
        self.text = "{}\n{}\n{}\n{}\n{}".format(
            horizontal_line,
            vertical_line,
            "\n".join(main_texts),
            vertical_line,
            horizontal_line
        )
        self.theme = theme
        self.transform = transform
        return self._print()


    def confirm(self, text, theme="confirm", transform=None):
        answered = False
        self.text = "\n{} (s/n) ".format(text)
        self.transform = transform
        self._print()
        if self.format_only:
            return self.text
        while not answered:
            ret = input(self.text)
            if ret and ret[0].upper() in ["S", "N"]:
                answered = True
        return ret[0].upper() == "S"

    def choose(self, choices, theme="choose", transform=None):
        self.text = "\n"
        for i, choice in enumerate(choices):
            self.text += "{}. {}\n".format(i + 1, choice)
        answered = False
        self.theme = theme
        self.transform = transform
        self._print()
        if self.format_only:
            return self.text
        while not answered:
            try:
                ret = input(
                    "Selecione (1-{}): ".format(i - 1))
                if ret and int(ret) in range(1, i):
                    answered = True
            except ValueError:
                pass
        return ret


    def unitext(self, text, theme=None, transform=None):
        self.text = unidecode(text)
        return self._print()


    def progress(self, count, total, prefix='Lendo', theme=None,
                     suffix='Completo', barLength=50):
        formatStr = "{0:.2f}"
        percents = formatStr.format(100 * (count / float(total)))
        filledLength = int(round(barLength * count / float(total)))
        bar = '█' * filledLength + '-' * (barLength - filledLength)
        self.text = '\r{} |{}| {}% {} '.format(prefix, bar, percents, suffix)
        
        if not self.format_only:
            sys.stdout.write(self.text)
            sys.stdout.flush()

        return self.text



console = Console()
format_txt = Console(format_only=True)