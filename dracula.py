# -*- coding: utf-8 -*-
"""
    Dracula Theme v1.2.5

    https://github.com/zenorocha/dracula-theme

    Copyright 2016, All rights reserved

    Code licensed under the MIT license
    http://zenorocha.mit-license.org

    :author Rob G <wowmotty@gmail.com>
    :author Chris Bracco <chris@cbracco.me>
    :author Zeno Rocha <hi@zenorocha.com>
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace

class DraculaStyle(Style):

    background_color = "#282a36"
    default_style = ""

    styles = {
        Comment: "#6272a4",
        Comment.Hashbang: "#6272a4",
        Comment.Multiline: "#6272a4",
        Comment.Preproc: "#ff79c6",
        Comment.PreprocFile: "#ff79c6",
        Comment.Single: "#6272a4",
        Comment.Special: "#8be9fd",

        Generic: "#ff79c6",
        Generic.Deleted: "#ff5555",
        Generic.Emph: "#f1fa8c underline",
        Generic.Error: "#ff5555",
        Generic.Heading: "#bd93f9 bold",
        Generic.Inserted: "#50fa7b bold",
        Generic.Output: "#6272a4",
        Generic.Prompt: "#50fa7b",
        Generic.Strong: "#ffb86c",
        Generic.Subheading: "#bd93f9 bold",
        Generic.Traceback: "#ff5555",

        Error: "#ff5555",

        Invisibles: "#44475a",

        Keyword: "#ff79c6",
        Keyword.Constant: "#bd93f9",
        Keyword.Declaration: "#ff79c6 italic",
        Keyword.Namespace: "#ff79c6",
        Keyword.Pseudo: "#ff79c6",
        Keyword.Reserved: "#ff79c6",
        Keyword.Type: "#8be9fd",

        LineNumbers: "#6272a4",
        LineNumbers.Highlight: "#f8f8f2",

        Literal: "#ffb86c",
        Literal.Date: "#ffb86c",

        Name: "#f8f8f2",
        Name.Attribute: "#50fa7b",
        Name.Builtin: "#bd93f9 italic",
        Name.Builtin.Pseudo: "#bd93f9",
        Name.Class: "#8be9fd",
        Name.Constant: "#bd93f9",
        Name.Decorator: "#50fa7b",
        Name.Entity: "#ff79c6",
        Name.Exception: "#ff5555",
        Name.Function: "#50fa7b",
        Name.Function.Magic: "#bd93f9",
        Name.Label: "#8be9fd italic",
        Name.Namespace: "#f8f8f2",
        Name.Other: "#f8f8f2",
        Name.Tag: "#ff79c6",
        Name.Variable: "#f8f8f2 italic",
        Name.Variable.Class: "#8be9fd italic",
        Name.Variable.Global: "#f8f8f2 italic",
        Name.Variable.Instance: "#bd93f9 italic",
        Name.Variable.Magic: "#bd93f9",

        Number: "#bd93f9",
        Number.Bin: "#bd93f9",
        Number.Float: "#bd93f9",
        Number.Hex: "#bd93f9",
        Number.Integer: "#bd93f9",
        Number.Integer.Long: "#bd93f9",
        Number.Oct: "#bd93f9",

        Operator: "#ff79c6",
        Operator.Word: "#ff79c6",

        Other: "#f8f8f2",

        Punctuation: "#f8f8f2",

        String: "#f1fa8c",
        String.Backtick: "#50fa7b",
        String.Char: "#f1fa8c",
        String.Doc: "#f1fa8c",
        String.Double: "#f1fa8c",
        String.Escape: "#ff79c6",
        String.Heredoc: "#f1fa8c",
        String.Interpol: "#ff79c6",
        String.Other: "#f1fa8c",
        String.Regex: "#ff5555",
        String.Single: "#f1fa8c",
        String.Symbol: "#bd93f9",

        Text: "#f8f8f2",

        Whitespace: "#f8f8f2"
    }
