import re

def parseString(inputString):
    from UI.ui import Main
    
    with open(inputString, mode='r', encoding='utf_8') as myfile:
        parseStr = myfile.read()
    
    patternOfName = {'TextDrawCreate': r'TextDrawCreate\((\d+\.\d+), (\d+\.\d+), "([^"]+)"\)'}
    patterOfFont = {'TextDrawFont': r'TextDrawFont\(.*?, (\d+)\)'}
    
    groups = parseStr.split('\n\n')  # Assuming groups are separated by empty lines
    
    results = []
    
    for group in groups:
        textDrawText = re.search(patternOfName['TextDrawCreate'], group)
        textDrawFont = re.search(patterOfFont['TextDrawFont'], group)
        
        if textDrawFont and int(textDrawFont.group(1)) in [0, 1, 2, 3] and textDrawText and textDrawText.group(3) != "_":
            # Define patterns for each TextDraw* function
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((\d+\.\d+), (\d+\.\d+), "([^"]+)"\)',
                'TextDrawFont': r'TextDrawFont\(.*?, (\d+)\)',
                'TextDrawLetterSize': r'TextDrawLetterSize\(.*?, (\d+\.\d+), (\d+\.\d+)\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawSetOutline': r'TextDrawSetOutline\(.*?, (\d+)\)',
                'TextDrawSetShadow': r'TextDrawSetShadow\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawColor': r'TextDrawColor\(.*?, (-?\d+)\)',
                'TextDrawBackgroundColor': r'TextDrawBackgroundColor\(.*?, (\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (\d+)\)',
                'TextDrawUseBox': r'TextDrawUseBox\(.*?, (\d+)\)',
                'TextDrawSetProportional': r'TextDrawSetProportional\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }
            
            # Order of fields in the result string
            fieldOrder = [
                'TextDrawCreate', 'TextDrawTextSize', 'TextDrawFont',
                'TextDrawLetterSize', 'TextDrawColor', 'TextDrawBackgroundColor',
                'TextDrawSetOutline', 'TextDrawSetShadow', 'TextDrawAlignment',
                'TextDrawSetSelectable'
            ]

            result = ["0"]

            # Dictionary to hold extracted values
            extracted_values = {key: None for key in fieldOrder}

            # Process each pattern and store the match in the dictionary
            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            # Append the extracted values in the correct order, skipping the text value from TextDrawCreate
            for key in fieldOrder:
                if extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])  # Append only the first two values
                    else:
                        result.extend(extracted_values[key])

            # Adding the TextDrawText value to the result
            if textDrawText:
                result.extend(["-1", textDrawText.group(3)])

            results.append(" ".join(result))
        
        elif textDrawFont and int(textDrawFont.group(1)) in [0, 1, 2, 3] and textDrawText and textDrawText.group(3) == "_":
            # Define patterns for each TextDraw* function
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((\d+\.\d+), (\d+\.\d+), "([^"]+)"\)',
                'TextDrawLetterSize': r'TextDrawLetterSize\(.*?, (\d+\.\d+), (\d+\.\d+)\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }

            # Order of fields in the result string
            fieldOrder = [
                'TextDrawCreate', 'TextDrawLetterSize', 'TextDrawTextSize',
                'TextDrawBoxColor', 'TextDrawAlignment', 'TextDrawSetSelectable'
            ]

            result = ["0"]

            # Dictionary to hold extracted values
            extracted_values = {key: None for key in fieldOrder}

            # Process each pattern and store the match in the dictionary
            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            # Append the extracted values in the correct order
            for key in fieldOrder:
                if extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])  # Append only the first two values
                    elif key == 'TextDrawTextSize':
                        result.append(extracted_values[key][1])  # Append the second value (width)
                    elif key == 'TextDrawLetterSize':
                        result.append(extracted_values[key][1])  # Append only the second value (height)
                    else:
                        result.append(extracted_values[key][0])  # Append only the value

            # Add the static values at the end
            result.extend(["0", "-1"])

            results.append(" ".join(result))
        elif textDrawFont and int(textDrawFont.group(1)) == 4:
            # Define patterns for TextDrawFont == 4
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((\d+\.\d+), (\d+\.\d+), "([^"]+)"\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)'
            }
            
            # Order of fields in the result string
            fieldOrder = [
                '0', 'TextDrawCreate', 'TextDrawTextSize', 'TextDrawTextSize',
                'TextDrawBoxColor', 'TextDrawAlignment', '2', 'TextDrawSetSelectable', '-1', 'TextDrawCreate'
            ]

            result = []

            # Dictionary to hold extracted values
            extracted_values = {key: None for key in fieldOrder}

            # Process each pattern and store the match in the dictionary
            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()

            # Append the extracted values in the correct order
            for key in fieldOrder:
                if key in ["0", "2", "-1"]:
                    result.append(key)
                elif extracted_values[key]:
                    if key == 'TextDrawCreate':
                        if len(result) == 1:  # For the first occurrence
                            result.extend(extracted_values[key][:2])  # Append only the first two values
                        else:
                            result.append(extracted_values[key][2])  # Append the third value
                    elif key == 'TextDrawTextSize':
                        result.append(extracted_values[key][0] if len(result) == 3 else extracted_values[key][1])  # Append the first value for the first occurrence and the second value for the second occurrence
                    elif key == 'TextDrawBoxColor' or key == 'TextDrawAlignment' or key == 'TextDrawSetSelectable':
                        if len(extracted_values[key]) >= 1:
                            result.append(extracted_values[key][0])  # Append the first value

            results.append(" ".join(result))
        elif textDrawFont and int(textDrawFont.group(1)) == 5:
            patterns = {
                'TextDrawCreate': r'TextDrawCreate\((\d+\.\d+), (\d+\.\d+), "([^"]+)"\)',
                'TextDrawTextSize': r'TextDrawTextSize\(.*?, (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawBoxColor': r'TextDrawBoxColor\(.*?, (\d+)\)',
                'TextDrawAlignment': r'TextDrawAlignment\(.*?, (\d+)\)',
                'TextDrawSetSelectable': r'TextDrawSetSelectable\(.*?, (\d+)\)',
                'TextDrawSetPreviewModel': r'TextDrawSetPreviewModel\(.*?, (\d+)\)',
                'TextDrawSetPreviewRot': r'TextDrawSetPreviewRot\(.*?, (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+)\)',
                'TextDrawColor': r'TextDrawColor\(.*?, (-?\d+)\)',
                'TextDrawBackgroundColor': r'TextDrawBackgroundColor\(.*?, (\d+)\)'
            }
            
            fieldOrder = [
                '0', 'TextDrawCreate', 'TextDrawTextSize', 'TextDrawBoxColor',
                'TextDrawAlignment', '1', 'TextDrawSetPreviewModel', 'TextDrawSetPreviewRot',
                'TextDrawColor', 'TextDrawBackgroundColor', 'TextDrawSetSelectable', '-1'
            ]
            
            result = []
            
            extracted_values = {key: None for key in fieldOrder}
            
            for key, pattern in patterns.items():
                match = re.search(pattern, group)
                if match:
                    extracted_values[key] = match.groups()
            
            for key in fieldOrder:
                if key in ["0", "1", "-1"]:
                    result.append(key)
                elif extracted_values[key]:
                    if key == 'TextDrawCreate':
                        result.extend(extracted_values[key][:2])
                    elif key == 'TextDrawTextSize':
                        result.extend(extracted_values[key])  # Append both values for TextDrawTextSize
                    elif key == 'TextDrawSetPreviewRot':
                        # Append all values from TextDrawSetPreviewRot with formatting
                        result.extend([
                            val if i == 3 else re.sub(r'\.0*$', '', val) for i, val in enumerate(extracted_values[key])
                        ])
                    else:
                        # Remove zeros after the decimal point and the decimal point itself
                        result.append(re.sub(r'\.0+$|(\.\d+?)0+$', '', extracted_values[key][0]))
            
            results.append(" ".join(result))
    


    return Main.resultUI("\n".join(results))
