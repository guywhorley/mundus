# Example of Class Inheritance

class Animal

    attr_accessor :alive

    def initialize
        @alive = true
        puts "I'm alive!"
        self
    end #def

    def breathe
        puts "Inhale and exhale"
        self # Ruby returns the last evaluated statement thus the 'return' keyword is not neccessary
    end
end #class
