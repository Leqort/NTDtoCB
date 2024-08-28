import re


def parseString(inputString):
    from UI.ui import Main

    with open(inputString, mode='r', encoding='utf_8') as myfile:
        parseStr = myfile.read()

    patternOfName = {
        'TextDrawCreate': r'TextDrawCreate\((-?\d+\.\d+), (-?\d+\.\d+), "([^"]+)"\)'}
    patterOfFont = {'TextDrawFont': r'TextDrawFont\(.*?, (\d+)\)'}

    groups = parseStr.split('\n\n')

    results = []

    for group in groups:
        textDrawText = re.search(patternOfName['TextDrawCreate'], group)
        textDrawFont = re.search(patterOfFont['TextDrawFont'], group)

        # Text parse
        if textDrawFont and int(textDrawFont.group(1)) in [0, 1, 2, 3] and textDrawText and textDrawText.group(3) != "_":
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((-?\d+\.\d+), (-?\d+\.\d+), "([^"]+)"\)',
                'TextDrawFont': r'TextDrawFont\(.*?, (\d+)\)',
                'TextDrawLetterSize': r'TextDrawLetterSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawSetOutline': r'TextDrawSetOutline\(.*?, (\d+)\)',
                'TextDrawSetShadow': r'TextDrawSetShadow\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawColor': r'TextDrawColor\(.*?, (-?\d+)\)',
                'TextDrawBackgroundColor': r'TextDrawBackgroundColor\(.*?, (-?\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (-?\d+)\)',
                'TextDrawUseBox': r'TextDrawUseBox\(.*?, (\d+)\)',
                'TextDrawSetProportional': r'TextDrawSetProportional\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }

            fieldOrder = [
                'TextDrawCreate', 'TextDrawTextSize', 'TextDrawFont',
                'TextDrawLetterSize', 'TextDrawColor', 'TextDrawBackgroundColor',
                'TextDrawSetOutline', 'TextDrawSetShadow', 'TextDrawAlignment',
                'TextDrawSetSelectable'
            ]

            result = ["0"]

            extracted_values = {key: None for key in fieldOrder}

            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            for key in fieldOrder:
                if extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])
                    elif key == 'TextDrawAlignment' and extracted_values[key][0] == '1':
                        result.append('3')
                    else:
                        result.extend(extracted_values[key])

            if textDrawText:
                result.extend(["-1", textDrawText.group(3)])

            results.append(" ".join(result))

        # Box parse
        elif textDrawFont and int(textDrawFont.group(1)) in [0, 1, 2, 3] and textDrawText and textDrawText.group(3) == "_":
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((-?\d+\.\d+), (-?\d+\.\d+), "([^"]+)"\)',
                'TextDrawFont': r'TextDrawFont\(.*?, (\d+)\)',
                'TextDrawLetterSize': r'TextDrawLetterSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawSetOutline': r'TextDrawSetOutline\(.*?, (\d+)\)',
                'TextDrawSetShadow': r'TextDrawSetShadow\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawColor': r'TextDrawColor\(.*?, (-?\d+)\)',
                'TextDrawBackgroundColor': r'TextDrawBackgroundColor\(.*?, (-?\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (-?\d+)\)',
                'TextDrawUseBox': r'TextDrawUseBox\(.*?, (\d+)\)',
                'TextDrawSetProportional': r'TextDrawSetProportional\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }

            fieldOrder = [
                'TextDrawCreate', '0', 'TextDrawTextSize', 'TextDrawFont', '0',
                'TextDrawLetterSize', 'TextDrawBoxColor', 'TextDrawBackgroundColor',
                'TextDrawSetOutline', 'TextDrawSetShadow', 'TextDrawAlignment',
                'TextDrawSetSelectable'
            ]

            result = ["0"]

            extracted_values = {key: None for key in fieldOrder}

            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            for key in fieldOrder:
                if key == '0':
                    result.append('0')
                elif extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])
                    elif key == 'TextDrawTextSize':
                        result.append(extracted_values[key][1])
                    elif key == 'TextDrawLetterSize':
                        result.append(extracted_values[key][1])
                    else:
                        result.append(extracted_values[key][0])

            result.extend(["-1", "_"])

            results.append(" ".join(result))

        # Sprite parse
        elif textDrawFont and int(textDrawFont.group(1)) == 4:
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((-?\d+\.\d+), (-?\d+\.\d+), "([^"]+)"\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (-?\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }

            fieldOrder = [
                'TextDrawCreate', 'TextDrawTextSize', 'TextDrawTextSize',
                '0xFFFFFFFF', 'TextDrawAlignment', '2', 'TextDrawSetSelectable', '-1', 'TextDrawCreate'
            ]

            result = ["0"]

            extracted_values = {key: None for key in fieldOrder}

            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            for key in fieldOrder:
                if key in ["2", "-1", "0xFFFFFFFF"]:
                    result.append(key)
                elif extracted_values[key]:
                    if key == 'TextDrawCreate':
                        if len(result) == 1:
                            result.extend(extracted_values[key][:2])
                        else:
                            result.append(extracted_values[key][2])
                    elif key == 'TextDrawTextSize':
                        result.append(extracted_values[key][0] if len(
                            result) == 3 else extracted_values[key][1])
                    elif key == 'TextDrawBoxColor' or key == 'TextDrawAlignment' or key == 'TextDrawSetSelectable':
                        if len(extracted_values[key]) >= 1:
                            result.append(extracted_values[key][0])

            results.append(" ".join(result))

        # Model parse
        elif textDrawFont and int(textDrawFont.group(1)) == 5:
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((-?\d+\.\d+), (-?\d+\.\d+), "([^"]+)"\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (-?\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)',
                'TextDrawSetPreviewModel': r'TextDrawSetPreviewModel\(.*?, (\d+)\)',
                'TextDrawSetPreviewRot': r'TextDrawSetPreviewRot\(.*?, (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawColor': r'TextDrawColor\(.*?, (-?\d+)\)',
                'TextDrawBackgroundColor': r'TextDrawBackgroundColor\(.*?, (-?\d+)\)'
            }

            fieldOrder = [
                'TextDrawCreate', 'TextDrawTextSize', 'TextDrawBoxColor',
                'TextDrawAlignment', '1', 'TextDrawSetPreviewModel', 'TextDrawSetPreviewRot',
                'TextDrawColor', 'TextDrawBackgroundColor', 'TextDrawSetSelectable', '-1'
            ]

            result = ["0"]

            extracted_values = {key: None for key in fieldOrder}

            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            for key in fieldOrder:
                if key in ["1", "-1"]:
                    result.append(key)
                elif extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])
                    elif key == 'TextDrawTextSize':
                        result.extend(extracted_values[key])
                    elif key == 'TextDrawSetPreviewRot':
                        result.extend([
                            val if i == 3 else re.sub(r'\.0*$', '', val) for i, val in enumerate(extracted_values[key])
                        ])
                    else:
                        result.append(re.sub(r'\.0+$|(\.\d+?)0+$',
                                      '', extracted_values[key][0]))

            results.append(" ".join(result))

    return Main.resultUI("\n".join(results))
