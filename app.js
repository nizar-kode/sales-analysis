function fetchUser() {
    return {
        id: 1,
        name: "Nizar",
        role: "Data Analyst"
    };
}

function displayUser(user) {
    console.log("User Info:");
    console.log(`Name: ${user.name}`);
    console.log(`Role: ${user.role}`);
}

const user = fetchUser();
displayUser(user);