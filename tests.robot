*** Variables ***
@{list}    one    two    three
&{dict}    key=value

*** Test Cases ***
Old FOR to be updated
    :FOR    ${animal}    IN    cat    dog    cow
    \    Log    Inside loop
    \    Log    ${animal}
    Log    Outside loop

    :FOR    ${animal}    IN    @{list}
    \    Log    ${animal}

Broken old FOR to be updated
    :FOR    ${animal}    IN    cat    dog    cow
        Log    ${animal}

New FOR to be preserved
    FOR    ${animal}    IN    cat    dog    cow
        Log to console    ${animal}
    END

Item access to be updated
    Log Many    @{list}[0]    &{dict}[key]    @{list}[0] &{dict}[key]

Upacking syntax to be preserved
    Log Many    @{list}       &{dict}

Mixed updates
    :FOR    ${x}    IN    @{list}[0]    @{list}
    \    Log Many    @{list}[0]    @{list}    &{dict}[key]    &{dict}
    Log    @{list}[0] @{list} &{dict}[key] &{dict}
